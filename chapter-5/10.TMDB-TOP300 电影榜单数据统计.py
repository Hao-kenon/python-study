import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']


def load_data(file_path: str) -> pd.DataFrame:
    """加载并返回电影数据。

    Args:
        file_path: CSV 文件路径

    Returns:
        包含电影名、年份、上映时间、类型、评分、语言的 DataFrame
    """
    return pd.read_csv(
        file_path,
        usecols=['电影名', '年份', '上映时间', '类型', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )


def create_figure() -> tuple[plt.Figure, list[Axes]]:
    """创建 2x2 子图布局。

    Returns:
        包含 Figure 对象和 4 个 Axes 对象的元组
    """
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300 电影榜单统计分析', fontsize=23, x=0.5, y=1)
    plt.subplots_adjust(hspace=1, wspace=0.3)
    return fig, [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]


def plot_yearly_count(data: pd.DataFrame, ax: Axes) -> None:
    """绘制历年电影上映数量统计折线图。

    Args:
        data: 电影数据 DataFrame
        ax: matplotlib Axes 对象
    """
    # 缺失值处理：用上映时间前 4 位补全年份缺失值
    data['年份'] = data['年份'].fillna(data['上映时间'].str[0:4])

    # 按年统计
    year_count = data.groupby('年份')['年份'].count()

    # 组装 x/y 数据
    min_year, max_year = year_count.index.min(), year_count.index.max()
    x = list(range(min_year, max_year + 1))
    y = [int(year_count.get(i, 0)) for i in x]

    # 绘制折线图
    ax.plot(x, y, c='g')
    ax.set_title('历年电影上映数量', fontsize=18)
    ax.set_xlabel('年份', fontsize=16)
    ax.set_ylabel('上映数量', fontsize=16)
    ax.set_xticks(x[::10])
    ax.set_yticks(range(0, 31, 3))
    ax.grid(linestyle='--')


def plot_language_count(data: pd.DataFrame, ax: Axes) -> None:
    """绘制不同语言电影数量对比柱状图。

    Args:
        data: 电影数据 DataFrame
        ax: matplotlib Axes 对象
    """
    language_count = data.groupby('语言')['语言'].count()
    languages = language_count.index.tolist()
    language_digits = language_count.values.tolist()

    ax.bar(languages, language_digits, color='g', width=0.4)
    ax.set_title('不同语言电影数量对比', fontsize=18)
    ax.set_xlabel('语言', fontsize=16)
    ax.set_ylabel('电影数量', fontsize=16)
    ax.tick_params(axis='x', rotation=90)
    ax.set_yticks(range(0, max(language_digits) + 1, 20))
    ax.grid(linestyle='--')


def plot_type_count(data: pd.DataFrame, ax: Axes) -> None:
    """绘制不同类型电影数量对比柱状图。

    Args:
        data: 电影数据 DataFrame
        ax: matplotlib Axes 对象
    """
    type_count: dict[str, int] = {}
    for types in data['类型'].str.split(',').tolist():
        for t in types:
            type_count[t] = type_count.get(t, 0) + 1

    x_types = list(type_count.keys())
    y_types = list(type_count.values())

    ax.bar(x_types, y_types, color='g', width=0.4)
    ax.set_title('不同类型电影数量对比', fontsize=18)
    ax.set_xlabel('类型', fontsize=16)
    ax.set_ylabel('电影数量', fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(linestyle='--')


def plot_rating_distribution(data: pd.DataFrame, ax: Axes) -> None:
    """绘制不同评分电影占比饼图。

    Args:
        data: 电影数据 DataFrame
        ax: matplotlib Axes 对象
    """
    rating_count = data.groupby('评分')['评分'].count()

    # 合并占比不到 2% 的小数据的数量到其他
    total = rating_count.sum()
    large_data: Series = rating_count[rating_count >= total * 0.02]
    small_data: Series = rating_count[rating_count < total * 0.02]

    if small_data.shape[0] > 0:
        large_data['其他'] = small_data.sum()

    rating = large_data.index.tolist()
    rating_digits = large_data.values.tolist()

    ax.pie(rating_digits, labels=rating, autopct='%1.1f%%')
    ax.set_title('不同评分电影数量占比', fontsize=18)
    ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.4))


def main():
    """主函数：加载数据、创建图表、保存并显示。"""
    # 加载数据
    data = load_data('data/movies.csv')

    # 创建画布
    fig, (ax1, ax2, ax3, ax4) = create_figure()

    # 绘制四个子图
    plot_yearly_count(data, ax1)
    plot_language_count(data, ax2)
    plot_type_count(data, ax3)
    plot_rating_distribution(data, ax4)

    # 保存并展示
    plt.savefig('data/TMDB_top300_movies_analysis.png')
    plt.show()


if __name__ == '__main__':
    main()
