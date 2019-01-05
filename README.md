# python_code
#### this is a repository to store my python training code
#### plt_loss_value.py用来提取1124.txt中的loss值
#### read_data_to_array.py用来提取表格excel1234.xlsx的第一列和第二列，并以数组的形式输出。

# python知识点查漏补缺

异常处理try，except
---
```
#异常处理：先尝试导入cPickle，如果失败，再导入pickle
try:
  import cPickle as pickle
except ImportError:
  import pickle
```
