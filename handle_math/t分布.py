'''
@Author: randolph
@Date: 2020-07-08 10:16:35
@LastEditors: randolph
@LastEditTime: 2020-07-08 10:20:38
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: python计算T分布下的置信区间
'''
import numpy as np
import scipy
from scipy import stats


def ci_t(data, confidence=0.95):
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sample_size = len(data)
    alpha = 1 - confidence
    t_score = scipy.stats.t.isf(alpha / 2, df=(sample_size - 1))

    ME = t_score * sample_std / np.sqrt(sample_size)
    lower_limit = sample_mean - ME
    upper_limit = sample_mean + ME

    print(str(confidence * 100) + '%% Confidence Interval: ( %.2f, %.2f)' % (lower_limit, upper_limit))
    return lower_limit, upper_limit


X1 = np.array([14.65, 14.95, 8.49, 9.51, 10.23, 2.75])
ci_t(X1)
