import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
def fun_p1_fengxian_k_means():
    """第一问风险值聚类"""
    df_data = pd.read_csv('output_problem_1/fengxian.csv')
    list2 = []
    for i in df_data.values:
        for m in i:
            list2.append(m)
    list1 = list(np.arange(114))
    K = 4
    p_list = np.stack([list1, list2], axis=1)
    index = np.random.choice(len(p_list), size=K)
    print(index)
    centeroid = p_list[index]
    print(centeroid)
    plt.scatter(23, 0.513, color='red', marker='x', label='K-means风险值')
    plt.scatter(57, 0.774, color='red', marker='x')
    plt.scatter(93, 1.350, color='red', marker='x')
    plt.scatter(113, 2.712, color='red', marker='x')
    plt.plot(list1, list2, '.', color='b', alpha=0.5, label='风险值')
    plt.legend()
    plt.xlim(0, 123)
    plt.ylim(0, 3)
    plt.xlabel('各个企业', fontsize=12)
    plt.ylabel('风险值', fontsize=12)
    plt.savefig('./output_figures/problem_1_fengxian_k-means.png', dpi=400)
    plt.show()
def fun_p2_fengxian_k_means():
    """第二问风险值聚类"""
    df_data = pd.read_csv('./output_problem_2/k_means_fengxian.csv')
    list2 = []
    for i in df_data.values:
        for m in i:
            list2.append(m)
    list1 = list(np.arange(267))
    K = 4
    p_list = np.stack([list1, list2], axis=1)
    index = np.random.choice(len(p_list), size=K)
    print(index)
    centeroid = p_list[index]
    print(centeroid)
    plt.scatter(63, 0.439, color='red', marker='x', label='K-means风险值')
    plt.scatter(143, 0.574, color='red', marker='x')
    plt.scatter(242, 0.898, color='red', marker='x')
    plt.plot(list1, list2, '.', color='b', alpha=0.5, label='风险值')
    plt.legend()
    plt.xlim(0, 270)
    plt.ylim(0, 1.1)
    plt.xlabel('各个企业', fontsize=12)
    plt.ylabel('风险值', fontsize=12)
    plt.savefig('./output_figures/problem_2_fengxian_k-means.png', dpi=400)
    plt.show()
def fun_p3_fengxian_k_means():
    filename = './fujian3/result_five_years.csv'
    df_1 = pd.read_csv(filename, encoding='GBK')
    y = df_1['风险值']
    fig, axes = plt.subplots(1)
    axes.plot(y, '<', color='blue', alpha=0.5, label='折线图', linestyle='-',
              marker='.', markerfacecolor='blue', markersize=10)
    plt.scatter(2.8, 0.739, color='red', marker='x', label='K-means风险值')
    plt.scatter(10.12, 0.374, color='red', marker='x')
    plt.scatter(20.449, 0.498, color='red', marker='x')
    axes.legend(loc='best')
    plt.savefig('./output_figures/problem_3_fengxian_k-means.png', dpi=400)
    plt.show()
def fun_nianlilv_ABCD():
    """第一问的拟合年利率和评级ABCD方程"""
    filename = './fujian3/data.csv'
    df_1 = pd.read_csv(filename, encoding='UTF-8')  # 导入指定列
    x = df_1['年利率']
    y = df_1['A']
    z = df_1['B']
    w = df_1['C']
    z1 = np.polyfit(x, y, 2)  # 用3次多项式拟合
    z2 = np.polyfit(x, z, 2)  # 用3次多项式拟合
    z3 = np.polyfit(x, w, 2)  # 用3次多项式拟合
    p1 = np.poly1d(z1)
    p2 = np.poly1d(z2)
    p3 = np.poly1d(z3)
    yvals = p1(x)  # 也可以使用yvals=np.polyval(z1,x)
    zvals = p1(x)  # 也可以使用yvals=np.polyval(z1,x)
    wvals = p1(x)  # 也可以使用yvals=np.polyval(z1,x)
    print('拟合后的年利率和评级ABCD客户流失率方程分别为：')
    print('y = \n', p1)  # 在屏幕上打印拟合多项式
    print('z = \n', p2)  # 在屏幕上打印拟合多项式
    print('w = \n', p3)  # 在屏幕上打印拟合多项式
    fig, axes = plt.subplots(2, 2)
    # 贷款年利率 评级A
    axes[0, 0].plot(x, y, '.', label='实际数据')
    axes[0, 0].plot(x, yvals, 'r', label='拟合图像')
    axes[0, 0].set_xlabel('贷款年利率')  # , fontsize=15
    axes[0, 0].set_ylabel('评级A客户流失率')
    axes[0, 0].legend(loc='upper left')
    axes[0, 0].text(0.058, 0.15, p1)
    # 贷款年利率 评级B
    axes[0, 1].plot(x, z, '.', label='实际数据')
    axes[0, 1].plot(x, zvals, 'b', label='拟合图像')
    axes[0, 1].set_xlabel('贷款年利率')  # , fontsize=15
    axes[0, 1].set_ylabel('评级B客户流失率')
    axes[0, 1].legend(loc='upper left')
    axes[0, 1].text(0.058, 0.15, p2)
    # 贷款年利率 评级C
    axes[1, 0].plot(x, w, '.', label='实际数据')
    axes[1, 0].plot(x, wvals, 'green', label='拟合图像')
    axes[1, 0].set_xlabel('贷款年利率')  # , fontsize=15
    axes[1, 0].set_ylabel('评级C客户流失率')
    axes[1, 0].legend(loc='upper left')
    axes[1, 0].text(0.058, 0.15, p3)
    plt.savefig('./output_figures/problem_1_ABCD_jinglilv.png')
    plt.show()
def run_main():
    fun_p1_fengxian_k_means()
    fun_p2_fengxian_k_means()
    fun_p3_fengxian_k_means()
    fun_nianlilv_ABCD()
if __name__ == '__main__':
    run_main()