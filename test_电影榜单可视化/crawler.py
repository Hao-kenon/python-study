import os
import re
import csv

import requests
from lxml import html

# 常量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIE_LIST_FILE = os.path.join(BASE_DIR, "data", "movie_list.csv")
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"  # 第一页
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"  # 第二页及之后

FIELDS = ["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "宣传语", "描述"]


# 保存所有电影数据为 csv 文件
def save_all_movies(all_movies):
    os.makedirs(os.path.dirname(MOVIE_LIST_FILE), exist_ok=True)
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(all_movies)
    print(f"已保存 {len(all_movies)} 条数据到 {MOVIE_LIST_FILE}")


# 提取电影年份（去掉括号）
def get_movie_years(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ""
    return movie_year.replace("(", "").replace(")", "")


# 提取上映时间（形如 2024-01-01）
def get_movie_date(movie_date):
    movie_date = movie_date[0].strip() if movie_date else ""
    match = re.search(r"\d{4}-\d{2}-\d{2}", movie_date)
    return match.group() if match else ""


# 提取时长，统一换算成分钟（如 "2h 22m" -> 142）
def get_movie_runtimes(movie_runtimes):
    movie_runtime = movie_runtimes[0].strip() if movie_runtimes else ""
    h_res = re.search(r"(\d+)h", movie_runtime)
    m_res = re.search(r"(\d+)m", movie_runtime)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m


# 获取单部电影详情，返回字典
def get_movie_info(movie_info_url):
    response = requests.get(movie_info_url, timeout=60)
    movie_doc = html.fromstring(response.text)

    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_date = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    movie_runtimes = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movie_writers = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")

    return {
        "电影名": movie_names[0].strip() if movie_names else "",
        "年份": get_movie_years(movie_years),
        "上映时间": get_movie_date(movie_date),
        "类型": ",".join(movie_tags) if movie_tags else "",
        "时长": get_movie_runtimes(movie_runtimes),
        "评分": movie_scores[0].strip() if movie_scores else "",
        "语言": movie_languages[0].strip() if movie_languages else "",
        "导演": ",".join(movie_directors) if movie_directors else "",
        "作者": ",".join(movie_writers) if movie_writers else "",
        "宣传语": movie_slogans[0].strip() if movie_slogans else "",
        "描述": movie_descriptions[0].strip() if movie_descriptions else "",
    }


# 主函数：爬取前 N 页榜单，保存为 csv
def main(max_pages=5):
    all_movies = []
    for page_num in range(1, max_pages + 1):
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            params = (
                f"air_date.gte=&air_date.lte=&certification=&certification_country=SG&debug="
                f"&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false"
                f"&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}"
                f"&primary_release_date.gte=&primary_release_date.lte=&region="
                f"&release_date.gte=&release_date.lte=2027-02-15&show_me=everything"
                f"&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10"
                f"&vote_count.gte=300&watch_region=SG&with_genres=&with_keywords=&with_networks="
                f"&with_origin_country=&with_original_language=&with_watch_monetization_types="
                f"&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400"
            )
            response = requests.post(TMDB_TOP_URL_2, params, timeout=60)

        print(f"正在爬取第 {page_num} 页...")
        document = html.fromstring(response.text)
        movie_list = document.xpath(
            "//div[contains(@class,'w-full') and contains(@class,'rounded-xl') and contains(@class,'border-gray-200')]"
        )

        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                all_movies.append(get_movie_info(movie_info_url))

    save_all_movies(all_movies)
    return all_movies


if __name__ == "__main__":
    main()
