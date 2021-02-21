"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p92 - 리스트 내포 예
"""

x = [2, 4, 1, 5, 7]

lst = [i ** 2 for i in x]
print(lst)

num = list(range(1, 11))
print(num)

lst2 = [i*2 for i in num if i % 2 ==0]
print(lst2)