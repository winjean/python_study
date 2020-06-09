#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='SimHei', size=13)
plt.rc('axes', unicode_minus='false')


def pie_chart(title, labels, sizes, explode):
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

    plt.axis('equal')
    plt.title(title)
    plt.show()


def bar_chart(title, xlabel, ylabel, xdata):
    # data = pd.read_excel("d:/winjean.xls", sheet_name=0, header=None)
    data = pd.read_excel("d:/winjean.xls", sheet_name=0, header=0, index_col=0)
    mm = data.sum()

    # 4个用户 0 1 2 3
    # the x locations for the groups
    ind = np.arange(len(xdata))
    # 设置宽度
    width = 0.35

    # '#008000'
    plt.bar(ind, mm, width, color='g', label='sum num')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    # 设置底部名称
    # 旋转40度
    plt.xticks(ind + width / 2, xdata, rotation=40)
    plt.yticks(None, None, rotation=10)
    # PNG文件--dpi是每英寸空间中包含的点的数量
    # plt.savefig('test', dpi=600)
    plt.show()


# 极坐标
def polar_chart():
    n = 20
    theta = np.linspace(0.0, 2 * np.pi, n, endpoint=False)
    radii = 10 * np.random.rand(n)
    width = np.pi / 4 * np.random.rand(n)

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    plt.show()


def scatter_chart(title):

    fig, ax = plt.subplots()
    ax.plot(5 * np.random.randn(5), 5 * np.random.randn(5), 'o')
    ax.set_title(title)
    # plt.savefig("scatter")
    plt.show()


def grid_chart(title):

    plt.subplot2grid((3, 3), (0, 0), colspan=3)
    plt.subplot2grid((3, 3), (1, 0), colspan=2)
    plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    plt.subplot2grid((3, 3), (2, 0))
    plt.subplot2grid((3, 3), (2, 1))
    # plt.savefig("scatter")
    plt.show()


def main():
    # 饼图
    # pie_chart(u'饼图', ['aa', 'bb', 'Dogs', 'Logs'], [15, 30, 45, 10], (0, 0.05, 0, 0.05))

    # 柱状图
    # bar_chart(u'电力窃漏电用户自动识别--总耗电量', u"用户名", u"总耗电量", [u'用户A', u'用户B', u'用户C', u'用户D'])

    # 极坐标
    # polar_chart()

    # 散点图
    # scatter_chart(u'散点图')

    grid_chart(u"aaa")


if __name__ == '__main__':
    main()
