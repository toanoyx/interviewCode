"""
给定几个国家字符串，首先将其按首字母字典顺序排序，再按照给定国家字符串逆序排序。
输入：China India England America
输出：America China England India
输入：China
输出：China America India England
"""


countrys = input()    # 输入国家字符串
sort_countrys = sorted(countrys.split())
print(sort_countrys)    # 按字典顺序输出

selectCountry = input()    # 输入指定国家字符串
len = len(sort_countrys)
index = 0
for i in range(len):    # 记录指定国家的index位置
    if sort_countrys[i] == selectCountry:
        index = i

if index == len:    # 若指定国家是最后一个字符串，则直接逆序输出
    print(reversed(sort_countrys))
else:    # 往temp中逆序添加国家字符串,然后输出
    j = index
    temp = []
    while j >= 0:
        temp.append(sort_countrys[j])
        j -= 1
    j = len - 1
    while j > index:
        temp.append(sort_countrys[j])
        j -= 1
    print(temp)
