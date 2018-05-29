#把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
tuple1=tuple(1,2,3)
dict1=dict{tuple1}
set1=set(tuple1)
print('dict1  ',dict1)
print('set1  ',set1)

tuple2=tuple(1,[2,3])
dict2=dict{tuple2}
set2=set(tuple2)
print('dict2  ',dict2)
print('set2  ',set2)

'''
list有序可重复，可变
tuple有序可重复，不变，可插入list，但tuple成员不变，只是list值变动
dict无序不重复，key值不变，不能插入list
set无序不重复，key值不变,不能插入list
不可变只能插入不可变
'''
