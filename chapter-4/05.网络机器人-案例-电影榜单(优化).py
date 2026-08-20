import re

import requests
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE = "csv_data/movie_list2.csv"
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"# 默认访问第一页
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"# 第二页及之后

# 保存所有电影数据，保存为  csv 文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名","年份","上映时间","类型","时长","评分","语言","导演","作者","宣传语","描述"])
        writer.writeheader() #写入表头
        writer.writerows(all_movies)#写入数据






# 获取电影年份
def get_movie_years(movie_years):
    movie_year = movie_years[0].strip() if movie_years else''
    return movie_year.replace('(','').replace(')','')

# 获取电影上映时间
def get_movie_date(movie_date):
    movie_date = movie_date[0].strip() if movie_date else ''
    return re.search(r"\d{4}-\d{2}-\d{2}",movie_date).group()

# 获取电影时长
def get_movie_runtimes(movie_runtimes):
    movie_runtime = movie_runtimes[0].strip() if movie_runtimes else ''
    h_res = re.search(r"(\d+)h",movie_runtime)
    m_res = re.search(r"(\d+)m",movie_runtime)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h*60+m


# 获取电影数据
def get_movie_info(movie_info_url):
    print(f"发送请求{movie_info_url},获取电影详情......")
    # 1.发送请求，获取数据
    response = requests.get(movie_info_url,timeout=60)
    # 2.解析数据
    movie_doc = html.fromstring(response.text)
    # 电影名称
    movie_names = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    # 电影年份
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    # 上映时间
    movie_date = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='release']/text()")
    # 电影标签
    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='genres']/a/text()")
    # 电影时长
    movie_runtimes = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[@class='runtime']/text()")
    # 电影评分
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    # 语言
    movie_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    # 导演
    movie_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    # 作者
    movie_writers = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    # 电影简介
    movie_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")
    # Slogan
    movie_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[@class='tagline']/text()")

    #3.返回电影详情 - 字典
    movie_info = {
        "电影名":movie_names[0].strip() if movie_names else " ",
        "年份":get_movie_years(movie_years),
        "上映时间":get_movie_date(movie_date),
        "类型":",".join(movie_tags) if movie_tags else " ",
        "时长": get_movie_runtimes(movie_runtimes),
        "评分":movie_scores[0].strip() if movie_scores else " ",
        "语言":movie_languages[0].strip() if movie_languages else " ",
        "导演":",".join(movie_directors) if movie_directors else " ",
        "作者":",".join(movie_writers) if movie_writers else " ",
        "宣传语": movie_slogans[0].strip() if movie_slogans else " ",
        "描述":movie_descriptions[0].strip() if movie_descriptions else " ",
    }
    return movie_info

# 主函数，定义核心逻辑
def main():
    all_movies = []
    for page_num in range(1,6):
        # 1.发送请求，获取数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte=&air_date.lte=&certification=&certification_country=SG&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-15&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=SG&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     timeout=60)

        print(f"发送请求，获取第{page_num}页TMDB电影榜单数据......")

        # 2.解析数据
        document = html.fromstring(response.text)
        movie_list = document.xpath(
            "//div[contains(@class,'w-full') and contains(@class,'rounded-xl') and contains(@class,'border-gray-200')]")

        # 3.遍历电影列表，获取电影名称和评分
        for movie in movie_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                # 电影详情的url
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求，获取电影数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)
    # 4.保存数据为 csv 文件
    save_all_movies(all_movies)
if __name__ == '__main__':
    main()