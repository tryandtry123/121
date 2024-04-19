# %%
import pandas as pd

# 创建一个数据列表
data = [10, 20, 30, 40, 50]

# 创建一个索引列表
index = ['a', 'b', 'c', 'd', 'e']

# 创建Series对象
series_obj = pd.Series(data, index=index)

# 打印Series对象
print(series_obj)


# %%
# 按索引名获取数据
value_by_index = series_obj['c']  # 获取索引为'c'的数据
print("Value by index 'c':", value_by_index)

# 按位置获取数据
value_by_position = series_obj.iloc[2]  # 获取位置为2的数据
print("position :", value_by_position)

# %%
# 增加数据
series_obj['f'] = 4
print("after adding:\n",series_obj)
# 删除数据
del series_obj['a']
print("after deleting:\n",series_obj)
# 修改数据
series_obj['b'] = 5


print("after modifying:\n",series_obj)


# %%

# 基于数组创建DataFrame
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = ['row1', 'row2', 'row3']
columns = ['col1', 'col2', 'col3']
df_from_array = pd.DataFrame(data, index=index, columns=columns)
print(df_from_array)


# %%
# 基于字典创建DataFrame
data = {
    'col1': [1, 4, 7],
    'col2': [2, 5, 8],
    'col3': [3, 6, 9]
}
index = ['row1', 'row2', 'row3']
df_from_dict = pd.DataFrame(data, index=index)

print( df_from_dict)


# %%
# 创建一个Series对象
series_obj = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# 增加数据
series_obj['d'] = 4
print("After adding:\n", series_obj)

# 删除数据
series_obj = series_obj.drop('c')
print("\nAfter deleting:\n", series_obj)

# 修改数据
series_obj['b'] = 5
print("\nAfter modifying:\n", series_obj)

# %%
# 创建一个Series对象
series_obj = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# 重置索引，保留原始索引作为列
reset_series = series_obj.reset_index()
print(reset_series)

# 重置索引，不保留原始索引
reset_series_drop = series_obj.reset_index(drop=True)
print("\n", reset_series_drop)

# %%
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
}, index=['row1', 'row2', 'row3', 'row4'])
print("prim df:\n",df)

# 使用loc[]索引非连续的行和列
result_loc = df.loc[['row1', 'row3'], ['A', 'C']]
print("\n"*3,result_loc)

# %%
# 使用iloc[]索引非连续的行和列
result_iloc = df.iloc[[0, 2], [0, 2]]
print(result_iloc)

# %%
# 假设有以下DataFrame
df = pd.DataFrame({
    'A': [4, 1, 3, 2],
    'B': [8, 7, 5, 6],
    'C': [12, 11, 9, 10]
}, index=[3, 1, 2, 0])
print("primi df:\n",df)

# 按索引升序排序
df_sorted = df.sort_index()
print("\n",df_sorted)

