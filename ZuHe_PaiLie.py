import itertools
from itertools import permutations
import xlwt


#快速生成一个数字列表
List = list(range(1,36))
last_List = list(range(1,13))


# permutations()是排列函数
#推导式list = [返回值 主体函数 条件]
New_list = [ new_list  for new_list in permutations(List, 5)]
New_lastList = [ new_last_List for new_last_List in permutations(last_List,2)]
#组合函数将两个列表元素组合product
all_list = list(itertools.product(New_list, New_lastList))  #出现报错MemoryError 内存不足,扩容



#将结果写入表格并输出f = open(file,mode,encoding=‘utf8’)
# 1.创建excel表格类型文件
Data_all = xlwt.Workbook(encoding= "utf-8", style_compression= 0)
# 2.创建sheet表单
Sheet_01 = Data_all.add_sheet("all_data", cell_overwrite_ok= True)
#3.自定义列名
col = ('序号', '排列')
#4.将列表属性元组写入sheet表单中
for i in range(0,1):
    Sheet_01.write(0, i, col[i])
#5.将数据写入sheet表单中
for i in range(0,):
    date = all_list[i]
    for j in range(0,):
        Sheet_01.write(i+1, j, date(j))
#6.保存excel文件
savePath = "E:\数据汇总.xls"
Data_all.save(savePath)