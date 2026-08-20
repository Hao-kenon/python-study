import os
import sys

import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

DATA_FILE = os.path.join(BASE_DIR, "data", "movie_list.csv")

# 页面配置（必须是第一个 Streamlit 命令）
st.set_page_config(page_title="电影榜单可视化", page_icon="🎬", layout="wide")


@st.cache_data
def load_movies(path):
    """读取 csv 并做基础类型转换"""
    df = pd.read_csv(path, encoding="utf-8")
    df["评分"] = pd.to_numeric(df["评分"], errors="coerce")
    df["时长"] = pd.to_numeric(df["时长"], errors="coerce")
    df["年份"] = pd.to_numeric(df["年份"], errors="coerce")
    return df


df = load_movies(DATA_FILE)

st.title("🎬 电影榜单可视化")

# ---------- 侧边栏：筛选条件 ----------
st.sidebar.title("筛选条件")

keyword = st.sidebar.text_input("搜索电影名 / 导演", "")

all_genres = sorted({g.strip() for s in df["类型"].dropna() for g in str(s).split(",") if g.strip()})
selected_genres = st.sidebar.multiselect("类型筛选", all_genres)

if df["年份"].notna().any():
    min_year, max_year = int(df["年份"].min()), int(df["年份"].max())
    year_range = st.sidebar.slider("年份范围", min_year, max_year, (min_year, max_year))
else:
    year_range = None

sort_order = st.sidebar.radio("排序方式", ["评分从高到低", "评分从低到高", "年份从新到旧"])

if st.sidebar.button("🔄 重新爬取数据", help="重新请求 TMDB，需要联网且耗时较长"):
    from crawler import main as crawl

    with st.spinner("正在爬取 TMDB 榜单，请耐心等待..."):
        crawl()
    st.cache_data.clear()
    st.rerun()

# ---------- 应用筛选 ----------
filtered = df.copy()

if keyword:
    filtered = filtered[
        filtered["电影名"].fillna("").str.contains(keyword, case=False, regex=False)
        | filtered["导演"].fillna("").str.contains(keyword, case=False, regex=False)
    ]

if selected_genres:
    def has_any_genre(genres_str):
        genres = {g.strip() for g in str(genres_str).split(",") if g.strip()}
        return bool(genres & set(selected_genres))

    filtered = filtered[filtered["类型"].apply(has_any_genre)]

if year_range is not None:
    filtered = filtered[
        (filtered["年份"] >= year_range[0]) & (filtered["年份"] <= year_range[1])
    ]

if sort_order == "评分从高到低":
    filtered = filtered.sort_values("评分", ascending=False)
elif sort_order == "评分从低到高":
    filtered = filtered.sort_values("评分", ascending=True)
else:
    filtered = filtered.sort_values("年份", ascending=False)

# ---------- 顶部指标卡 ----------
distinct_genres = filtered["类型"].fillna("").str.split(",").explode().str.strip()
distinct_genres = distinct_genres[distinct_genres != ""]

c1, c2, c3, c4 = st.columns(4)
c1.metric("电影总数", len(filtered))
c2.metric("平均评分", f"{filtered['评分'].mean():.1f}" if filtered["评分"].notna().any() else "—")
c3.metric("平均时长(分钟)", f"{filtered['时长'].mean():.0f}" if filtered["时长"].notna().any() else "—")
c4.metric("类型数量", distinct_genres.nunique())

st.divider()

# ---------- 图表 / 表格 ----------
if filtered.empty:
    st.warning("没有符合条件的电影，请调整筛选条件。")
else:
    tab_chart, tab_table = st.tabs(["📊 图表", "📋 数据表格"])

    with tab_chart:
        left, right = st.columns(2)

        with left:
            st.subheader("评分分布")
            st.bar_chart(filtered["评分"].value_counts().sort_index())

        with right:
            st.subheader("类型 Top10")
            st.bar_chart(distinct_genres.value_counts().head(10))

        st.subheader("年份分布")
        st.bar_chart(filtered["年份"].value_counts().sort_index())

    with tab_table:
        st.dataframe(filtered, height=600)
