<center><img src="https://i.loli.net/2020/05/17/cZIP7ARlLJtXwkv.png" width="20%"></center>

## 如何进行性能分析

### 1. 逻辑上的时间复杂度和空间复杂度

举例：数据集包括1000人的人脸，每个人两个人脸图片。 新的一个人，判断能不能加入这个数据集（与元数据集中的人是否有重复）。
当数据集从1000人扩充到2000人时，时间复杂度$o(n)=1000^2$

```
for each_face in dataset:
     score(each_face,this_face)
 # 1001要算1000次,1000+1001+...+1999
```

优化1： 分男女，性别分开。

优化2：现在有多少人的多少人脸，就先预先把到网络的目标层给算出来，存在某个地方。

### 2. 内存估算

用存储空间模拟，防止OOM(Out of Memory)
举例：1000张图片，每张的分辨率1024x1024x3，数据类型是float32。

```python
import numpy as np
a = np.random.rand(1024*1024*3)
a = a.astype(np.float32)
np.save('C:\\Users\\yue\\Desktop\\a.npy', a)
```
![2020.png](https://i.loli.net/2020/02/09/LKBVb15CsiYEoGI.png)

### 3.显存
两个指标：**显存容量**，**GPU利用率**

![nvidia-smi.jpeg](https://i.loli.net/2020/02/09/aG7yiucBPdMlm81.jpg)

先把数据集读入，读入一个batch，再跑这个batch
```
all_imgs = [(img, label)]   # 有10w张图片
for i in range(1000000):
      batch_img, batch_label = generate_batch(all_imgs) # CPU
      sess.run(, feed_dict={batch_img, batch_label}) # GPU
```
因此可能会出现系统占显存数量高，但是显存利用率低的情况

提高显存利用率的三种方法：

（1）自己写gpu运算，把前面的一些操作也用gpu

（2）多线程

（3）**tf.data**

思路：
-  将一个epoch所有数据预处理好，写入一个磁盘文件
- 用tf.data 的一些API，自动的建立一个batch读取的机制

根据X_train制作tfrecords磁盘文件，这个文件包含是预处理后的矩阵，也就是之前输入的placehoder的那种
```
    dataset = tf.data.TFRecordDataset('./trans/tran.tfrecords')

    dataset = dataset.map(parse_function)
    dataset = dataset.shuffle(buffer_size=50000)
    dataset = dataset.batch(batch_size)
    iterator= dataset.make_initializable_iterator()
    next_element = iterator.get_next() #得到next_element这个tensor
```
每一次运行 batch_train, batch_label  = sess.run(next_element)

然后如果整个tfrecords读完了，就会弹出tf.errors.OutOfRangeError，可以接收这个error，重启迭代器

详见示例代码resnet_mnist_tfdata.py

### 4.对编程语言的熟练度
不同的语言，调用不同的方法产生的性能差异是巨大（低级优化）。

举例:矩阵乘法
```python
import time
import numpy as np

def matrix_mul(mat1, mat2):
    ans_mat = []
    for mat1_row in mat1:
        ans_mat_row = []
        for mat2_col_ind in range(len(mat2[0])):
            mat2_col = mat2[:, mat2_col_ind]
            ans_mat_row.append( np.sum( np.multiply(mat1_row, mat2_col)  )   )
        ans_mat.append(ans_mat_row)
    return ans_mat

mat1 = np.random.rand(1024, 1024)
mat2 = np.random.rand(1024, 1024)

#以np.dot计算
start_time1 =time.time()
mat_ans1 = np.dot(mat1, mat2)
end_time1 = time.time()

#np.einsum
start_time2 =time.time()
mat_ans2 = np.einsum('ik,kj->ij', mat1, mat2)
end_time2 = time.time()

#自己进行底层实现
start_time3 =time.time()
mat_ans3 = matrix_mul(mat1, mat2)
end_time3 = time.time()

print(end_time1 - start_time1)
print(end_time2 - start_time2)
print(end_time3 - start_time3)

'''
结果
0.07811355590820312
0.5333499908447266
11.39245057106018
'''
```
#### Einsum in numpy：
1)矩阵转置 $B_{ij}=A_{ji}$
```python
B = np.einsum('ij->ji', [a])
```
2)矩阵求和 $b=\sum_{i}\sum_{j}A_{ij}$
```python
b = np.einsum('ij->', [a])
```
3)按列求和 $b_j=\sum_{i}A_{ij}$
```python
b = np.einsum('ij->j', [a])
```
4)按行求和 $b_i=\sum_{j}A_{ij}$
```python
b = np.einsum('ij->i', [a])
```
5)矩阵向量乘法 $c_i=\sum_{k}A_{ik}b_k$
```python
c = np.einsum('ik,k->i', [a, b])
```
6)矩阵相乘 $c_{ij}=\sum_{k}A_{ik}b_{kj}$
```python
c = np.einsum('ik,kj->ij', [a, b])
```
7)点积 $c=\sum_{i}a_ib_i$
```python
c = np.einsum('i,i->', [a, b])
```
8）批矩阵乘法 $c_{ijl}=\sum_{k}a_{ijk}b_{ikl}$
```python
c = np.einsum('ijk,ikl->ijl', [a, b])
```
$...$以此类推,可阅读[参考文件](https://rockt.github.io/2018/04/30/einsum)

### 5.模型大小
- 首先用tf.global_variables得到所有的参数
- 根据参数的shape做乘法，得到每个参数的数据量
- 把每个参数的数据量求和，得到总参数量
- 可以用之前的方法估算整个参数量的存储大小、占用内存的大小等等。

举例：resnet_mnist_tfdata.py中的参数量
```python
vars = tf.global_variables()
tot_params = 0
for each_var in vars:
    print(each_var)
    shape = each_var.get_shape()
    variable_params = 1
    for dim in shape:
        variable_params *= dim.value
    print(variable_params)
    tot_params += variable_params
print('total params: ', tot_params)
'''
结果：
<tf.Variable 'conv1/kernel:0' shape=(7, 7, 1, 64) dtype=float32_ref>
3136
<tf.Variable 'bn1/gamma:0' shape=(64,) dtype=float32_ref>
64
<tf.Variable 'bn1/beta:0' shape=(64,) dtype=float32_ref>
64
<tf.Variable 'bn1/moving_mean:0' shape=(64,) dtype=float32_ref>
64
...
<tf.Variable 'fc/bias/Adam:0' shape=(10,) dtype=float32_ref>
10
<tf.Variable 'fc/bias/Adam_1:0' shape=(10,) dtype=float32_ref>
10
total params:  1415904
'''
```
```python
import numpy as np
a = np.random.rand(1415904)
a = a.astype(np.float32)
np.save('C:\\Users\\yue\\Desktop\\result.npy', a)
```
