# Python 数字型|字符串

## 一：数字型

### 1. 出现浮点数结果的原因

1. 如果出现浮点数参与的计算，那最后得出来的结果就是：**浮点数**
2. 除法涉及精度问题，所以结果也会出现：**浮点数结果**



### ipython

1. 方便调试



## 二：字符串

### 1. 三种创建方式的原因

1. 单双引号的混用
2. 多行文本、注释、注解
3. 补充：查看源代码：command + 点击



### 2. 切片

1. 单个数字不能超出范围
2. 如果截取一段长度的：可以超过



### 3. 字符串内置函数

1. find：只会放回第一个出现的位置
2. 



### 4. Input 得到的数据类型都是 str

```python
In [72]: type(input())
1
Out[72]: str

In [73]: type(input())
[1, 2, 3, 4]
Out[73]: str

In [74]: type(input())
(1, 2, 3)
Out[74]: str

In [75]: type(input())
{1:2, 4:2}
Out[75]: str

In [76]: type(input())
{1, 2, 3, 4}
Out[76]: str
```

