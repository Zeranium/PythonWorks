"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p116 - builtins 함수와 import 함수 예
"""

dataset = list(range(1,6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

import statistics
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print('표본 분산=', statistics.variance(dataset))
print('표본 표준편차=', statistics.stdev(dataset))