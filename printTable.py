tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alicdadadafgae', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
                                                       ]


def printTable(lists):
    length = []
    # 找出每列所需要的整数长度
    for list in lists:  # 遍历传进来的列表
        temp = 0
        for elem in list:  # 遍历每个列表中列表的元素
            if len(elem) > temp:
                temp = len(elem) # 找出lists[]中最长的元素的值
        length.append(temp) # 将每个值放入列表中

    for j in range(len(lists[0])):
        for k in range(len(lists)):
            print(lists[k][j].rjust(length[k]) + '\t', end='') # 取消内层换行，用空格隔开
        print() # 外层换行


printTable(tableData)
