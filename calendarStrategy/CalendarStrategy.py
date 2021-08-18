__author__ = 'Teng Li'

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
定义工具函数
'''

def get_drawdown(p):
    """
    计算净值回撤
    """
    T = len(p)
    hmax = [p[0]]
    for t in range(1, T):
        hmax.append(np.nanmax([p[t], hmax[t - 1]]))
    dd = [p[t] / hmax[t] - 1 for t in range(T)]

    return dd


def cal_period_perf_indicator(adjnav):
    """
    计算区间业绩指标
    """

    if type(adjnav) == pd.DataFrame:
        res = pd.DataFrame(index=adjnav.columns, columns=['AnnRet', 'AnnVol', 'SR', 'MaxDD', 'Calmar'])
        for col in adjnav:
            res.loc[col] = cal_period_perf_indicator(adjnav[col])

        return res

    ret = adjnav.pct_change()
    annret = np.nanmean(ret) * 242
    annvol = np.nanstd(ret) * np.sqrt(242)
    sr = annret / annvol
    dd = get_drawdown(adjnav)
    mdd = np.nanmin(dd)
    calmar = annret / -mdd

    return [annret, annvol, sr, mdd, calmar]


def datestr2dtdate(datestr):
    # 日期格式转换：'yyyy-mm-dd'转为datetime.date
    return datetime.datetime.strptime(datestr, '%Y-%m-%d').date()


def date_count_in_mouth(dates):
    # 计算日期序列中每个日期在所在月中的序数
    cur_count = 1
    counts = [cur_count]
    for i in range(1,len(dates)):
        if dates[i].month == dates[i-1].month:
            cur_count = cur_count + 1
        else:
            cur_count = 1
        counts.append(cur_count)
    return counts


'''
main
'''

# 从csv文件获取指数价格数据
index_data = pd.read_csv('calendarStrategy/指数历史数据.csv').set_index('datetime')
index_data.index = [datestr2dtdate(e) for e in index_data.index]

# 设置回测参数
index_id = 'hs300' # 标的指数：'hs300' or 'csi500' or 'csi1000'
start_date = datetime.date(2012,1,1) # 回测起始日期
end_date = datetime.date(2021,7,27) # 回测截止日期
t1 = 1  # 每月持仓交易起始日，从1起
t2 = 5 # 每月持仓交易截止日，从1起


# 回测
df = index_data.loc[start_date:end_date,[index_id]]
df['index_ret'] = df[index_id].pct_change()
df['index'] = (1+df['index_ret']).cumprod()
df['date_count_in_month'] = date_count_in_mouth(df.index)
df['pos'] = [1 if (e>=t1 and e<=t2) else 0 for e in df['date_count_in_month']] # 昨收仓位
df['stgy_ret'] = df['pos'] * df['index_ret']
df['stgy'] = (1+df['stgy_ret']).cumprod()

# 回测结果展示
fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(2,1,1)
df.loc[:,['index','stgy']].plot(ax=ax1, grid=True, title='%s: t1=%d, t2=%d' % (index_id,t1,t2))
ax2 = fig.add_subplot(2,1,2)
df.loc[:,['pos']].plot(ax=ax2, grid=True)
res = cal_period_perf_indicator(df.loc[:,['index','stgy']])
print(res)