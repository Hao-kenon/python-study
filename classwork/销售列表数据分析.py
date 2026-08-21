from tkinter import font

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from narwhals import col
from pandas import Series

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

def load_data(file_path: str) -> pd.DataFrame:
    """加载并返回数据"""
    return pd.read_csv(file_path,nrows=50,usecols=['产品类别', '销售数量', '单价', '客户所在城市', '支付方式', '订单日期'])


def create_figure() -> tuple[plt.Figure, list[Axes]]:
    """创建并返回一个包含 2x2 子图的 Figure 和 Axes 列表"""
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,12),dpi=100)
    fig.suptitle('销售数据统计分析',fontsize=23,x=0.5,y=1)
    fig.subplots_adjust(hspace=1, wspace=0.3)
    return fig, [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]

def data_brush(data: pd.DataFrame) -> pd.DataFrame:
    data['单价'] = data['单价'].abs()
    data['订单日期'] = data['订单日期'].str.replace('/', '-')
    data['销售额'] = data['销售数量'] * data['单价']
    return data


def daily_sales(data: pd.DataFrame, ax: Axes) -> None:
    """按天统计销售数量并绘制折线图"""
    sales:Series = data.groupby('订单日期')['销售额'].sum()
    sales.index = sales.index.str[8::]

    x_date = sales.index.tolist()
    y_salse = sales.values.tolist()

    #绘制折线图
    ax.plot(x_date, y_salse, color='g')
    #设置标题和轴标签
    ax.set_title('每日销售额变化 2025-06',fontsize=15)
    ax.set_xlabel('日期', fontsize=14)
    ax.set_ylabel('销售数量', fontsize=14)
    #绘制网格
    ax.grid(linestyle='--')


def cities_sales(data: pd.DataFrame, ax: Axes) -> None:
    """按城市统计销售数量并绘制条形图"""
    cities_count: Series = data.groupby('客户所在城市')['销售数量'].sum()
    x_city = cities_count.index.tolist()
    y_cities_count = cities_count.values.tolist()

    #绘制柱状图
    ax.bar(x_city, y_cities_count, color='g')
    #设置标题和轴标签
    ax.set_title('不同城市销售数量对比', fontsize=15)
    ax.set_xlabel('城市', fontsize=14)
    ax.set_ylabel('销售数量', fontsize=14)
    #旋转X轴标签
    #设置网格
    ax.grid()


def type_sales(data: pd.DataFrame, ax: Axes) -> None:
    """按产品类别统计销售数量并绘制条形图"""
    products_count: Series = data.groupby('产品类别')['销售数量'].sum()
    x_products = products_count.index.tolist()
    y_products_count = products_count.values.tolist()

    #绘制饼图
    ax.pie(y_products_count, labels=x_products, autopct='%1.1f%%', startangle=140)
    #设置标题
    ax.set_title('不同产品类别销售数量比例', fontsize=15)
    #设置图例属性
    ax.legend(loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.2))


def payment_method_sales(data: pd.DataFrame, ax: Axes) -> None:
    """按支付方式统计销售数量并绘制饼图"""
    payment_count: Series = data.groupby('支付方式')['订单日期'].count()

    x_payment = payment_count.index.tolist()
    y_payment_count = payment_count.values.tolist()

    #绘制饼图
    ax.pie(y_payment_count, labels=x_payment, autopct='%1.1f%%', startangle=140)
    #设置标题
    ax.set_title('不同支付方式对应订单占比', fontsize=15)
    #设置图例属性
    ax.legend(loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.2))


def main():
    #加载数据
    data = load_data('data/sales.csv')

    #创建画布
    fig, (ax1, ax2, ax3, ax4) = create_figure()

    #数据预处理
    data = data_brush(data)

    #绘制四张子图
    daily_sales(data, ax1)
    cities_sales(data, ax2)
    type_sales(data, ax3)
    payment_method_sales(data, ax4)

    #保存并展示
    plt.savefig('data/sales_analysis.png')
    plt.show()

if __name__ == '__main__':
    main()
