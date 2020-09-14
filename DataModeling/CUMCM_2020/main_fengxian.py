import pandas as pd


def run_fengxian(path_1, path_2):
    """
        name：“求风险值函数”
        function: 将分组求和后的销项发票信息和进项发票信息合并; 求销售净利率
        path_1：销项发票
        path_2：进项发票
    """
    df_1 = pd.read_csv(path_1, encoding='UTF-8')  # 销项
    df_2 = pd.read_csv(path_2, encoding='UTF-8')  # 进项
    # 删除没用的列
    del df_1['发票号码']
    del df_1['开票日期']
    del df_1['购方单位代号']
    del df_2['发票号码']
    del df_2['开票日期']
    del df_2['销方单位代号']
    # 只保留发票状态中有效发票的行
    df_1 = df_1[(df_1['发票状态'].isin(['有效发票']))]
    df_2 = df_2[(df_2['发票状态'].isin(['有效发票']))]
    # 删除整个数据表中所有含有负值的行
    df_1 = df_1[df_1['金额'].apply(lambda x: x >= 0)]
    df_1 = df_1[df_1['税额'].apply(lambda x: x >= 0)]
    df_2 = df_2[df_2['金额'].apply(lambda x: x >= 0)]
    df_2 = df_2[df_2['税额'].apply(lambda x: x >= 0)]
    # 删除发票状态，为了后面的分组求和（中文求不了）
    del df_1['发票状态']
    del df_2['发票状态']
    # 分组求和
    df_1 = df_1.groupby('企业代号').sum()
    df_1 = df_1.rename(columns={'金额': '金额_销项', '税额': '税额_销项', '价税合计': '价税合计_销项'})
    df_2 = df_2.groupby('企业代号').sum()
    df_2 = df_2.rename(columns={'金额': '金额_进项', '税额': '税额_进项', '价税合计': '价税合计_进项'})
    # 合并两张表
    result = pd.concat([df_1, df_2], axis=1)
    # 求销售净利率
    result['净利润'] = result['金额_销项'] - result['金额_进项'] + result['税额_进项'] - result['税额_销项']
    result['销售收入'] = result['金额_销项']
    result['销售净利率'] = result['净利润'] / result['销售收入']
    # 求风险值
    result["exp_销售净利率"] = result["销售净利率"].apply(pd.np.exp)
    result['风险值'] = 1 / (result['exp_销售净利率'])
    return result

def run_fenxian_p3(path):
    """
        name：“求问题三的风险值”
        path：求出的风险文件路径
    """
    df = pd.read_csv(path, encoding='GBK')
    result = df
    result['净利润'] = result['突发影响函数值'](result['金额_销项'] - result['金额_进项'] + result['税额_进项'] - result['税额_销项'])
    result['销售收入'] = result['金额_销项']
    result['销售净利率'] = result['净利润'] / result['销售收入']
    # 求风险值
    result["exp_销售净利率"] = result["销售净利率"].apply(pd.np.exp)
    result['风险值'] = 1 / (result['exp_销售净利率'])

    return

def run_fenxian_qujian(path):
    """
        name：“求风险值函数区间”
        function: 【总年】将求出来的风险值去掉<1的【单年】不用
        path：求出的风险文件路径
    """
    df = pd.read_csv(path, encoding='GBK')
    result_fengxian_qujian = df
    # 将风险值大于1的去掉,只保留小于等于1的风险
    result_fengxian_qujian = result_fengxian_qujian[result_fengxian_qujian['风险值'].apply(lambda x: x <= 1)]
    return result_fengxian_qujian



def run_main():
    # 问题一 五年总风险值
    file_five_years_input = './fujian1/fujian1_input.csv'
    file_five_years_output = './fujian1/fujian1_output.csv'
    print_five = run_fengxian(file_five_years_output, file_five_years_input)
    print_five.to_csv('./output_problem_1/result_five_years.csv', encoding='GBK')
    five_qujian = run_fenxian_qujian('./output_problem_1/result_five_years.csv')
    five_qujian.to_csv('./output_problem_1/result_five_years_qujian.csv', encoding='GBK')
    # 问题二 五年总风险值
    file_five_years_input = './fujian2/fujian2_input.csv'
    file_five_years_output = './fujian2/fujian2_output.csv'
    print_five = run_fengxian(file_five_years_input, file_five_years_output)
    print_five.to_csv('./output_problem_2/result_five_years.csv', encoding='GBK')
    five_qujian = run_fenxian_qujian('./output_problem_2/result_five_years.csv')
    five_qujian.to_csv('./output_problem_2/result_five_years_qujian.csv', encoding='GBK')
    # 问题二 2017年风险
    file_2017_output = './fujian2/data_2017/fujian2_output_2017.csv'
    file_2017_input = './fujian2/data_2017/fujian2_input_2017.csv'
    print_2017 = run_fengxian(file_2017_output, file_2017_input)
    print_2017.to_csv('./output_problem_2/result_2017.csv', encoding='GBK')
    # 问题二 2018年风险
    file_2018_output = './fujian2/data_2018/fujian2_output_2018.csv'
    file_2018_input = './fujian2/data_2018/fujian2_input_2018.csv'
    print_2018 = run_fengxian(file_2018_output, file_2018_input)
    print_2018.to_csv('./output_problem_2/result_2018.csv', encoding='GBK')
    # 问题二 2019年风险
    file_2019_output = './fujian2/data_2019/fujian2_output_2019.csv'
    file_2019_input = './fujian2/data_2019/fujian2_input_2019.csv'
    print_2019 = run_fengxian(file_2019_output, file_2019_input)
    print_2019.to_csv('./output_problem_2/result_2019.csv', encoding='GBK')
    # 问题二 2020年风险
    file_2020_output = './fujian2/data_2020/fujian2_output_2020.csv'
    file_2020_input = './fujian2/data_2020/fujian2_input_2020.csv'
    print_2020 = run_fengxian(file_2020_output, file_2020_input)
    print_2020.to_csv('./output_problem_2/result_2020.csv', encoding='GBK')
    # # 问题三 总风险
    # file_fengxian_fx_shoudong = '手动整理之后的一张表'
    # p3_fengxian = run_fenxian_qujian(file_fengxian_fx_shoudong)
    # p3_fengxian.to_csv('./output_problem_3/result_fengxian_fx.csv', encoding='GBK')

if __name__ == '__main__':
    run_main()
