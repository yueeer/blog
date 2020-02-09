import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

tf.reset_default_graph()  # 防止存在already exit问题
mnist = input_data.read_data_sets('MNIST_data', one_hot=False)

def generate_tfrecords(mnist, output_path='./mnist_train_records'):
    writer = tf.python_io.TFRecordWriter(output_path)
    print(mnist.train.images.shape, mnist.train.labels.shape)
    train  = mnist.train.images.reshape(55000,28,28,1)
    labels = mnist.train.labels.reshape(55000)
    for ind, (file, label) in enumerate(zip(train, labels)):
        img_raw = file.tobytes()
        example = tf.train.Example(features=tf.train.Features(feature={
            'image_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw])),
            "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[label]))
        }))
        writer.write(example.SerializeToString())  # Serialize To String 转化为字节流存储在mnist_train_records
        if ind != 0 and ind % 1000 == 0:
            print("%d num imgs processed" % ind)
    writer.close()

# 先把下面的所有代码都注释一下，然后服务器上跑一下上面这个部分得到mnist_train_records

xs = tf.placeholder(tf.float32, [None, 28, 28, 1])  # 28x28 mnist.train.images:[None]*784
ys = tf.placeholder(tf.int64, [None, ])  # 10类 mnist.train.labels:[None]*10
ys_one_hot = tf.one_hot(ys, depth=10)
learning_rate = tf.placeholder(tf.float32)


def inception(input_tensor, kernel_size, filters, stage, is_training, reuse,
              kernel_initializer=tf.contrib.layers.variance_scaling_initializer()):
    filters1, filters2, filters3, filters4 = filters

    conv_name_1 = 'conv' + str(stage) + '_1'
    bn_name_1 = 'bn' + str(stage) + '_1'
    conv_1 = tf.layers.conv2d(input_tensor, filters1, kernel_size, use_bias=False, padding='SAME',
                              kernel_initializer=kernel_initializer, name=conv_name_1, reuse=reuse)
    bn_1 = tf.layers.batch_normalization(conv_1, training=is_training, name=bn_name_1, reuse=reuse)
    relu_1 = tf.nn.relu(bn_1)

    conv_name_2 = 'conv' + str(stage) + '_2'
    bn_name_2 = 'bn' + str(stage) + '_2'
    conv_2 = tf.layers.conv2d(relu_1, filters2, kernel_size, use_bias=False, padding='SAME',
                              kernel_initializer=kernel_initializer, name=conv_name_2, reuse=reuse)
    bn_2 = tf.layers.batch_normalization(conv_2, training=is_training, name=bn_name_2, reuse=reuse)
    relu_2 = tf.nn.relu(bn_2)

    conv_name_3 = 'conv' + str(stage) + '_3'
    bn_name_3 = 'bn' + str(stage) + '_3'
    conv_3 = tf.layers.conv2d(relu_2, filters3, kernel_size, use_bias=False, padding='SAME',
                              kernel_initializer=kernel_initializer, name=conv_name_3, reuse=reuse)
    bn_3 = tf.layers.batch_normalization(conv_3, training=is_training, name=bn_name_3, reuse=reuse)
    relu_3 = tf.nn.relu(bn_3)

    conv_name_4 = 'conv' + str(stage) + '_4'
    bn_name_4 = 'bn' + str(stage) + '_4'
    conv_4 = tf.layers.conv2d(relu_3, filters4, kernel_size, use_bias=False, padding='SAME',
                              kernel_initializer=kernel_initializer, name=conv_name_4, reuse=reuse)
    bn_4 = tf.layers.batch_normalization(conv_4, training=is_training, name=bn_name_4, reuse=reuse)
    relu_4 = tf.nn.relu(bn_4)

    x = tf.concat([relu_1, relu_2, relu_3, relu_4], -1)

    return x


def googlenet(input_tensor, is_training=True, pooling_and_fc=True, reuse=False,
              kernel_initializer=tf.contrib.layers.variance_scaling_initializer()):
    conv1 = tf.layers.conv2d(input_tensor, 64, (7, 7), strides=(2, 2), kernel_initializer=kernel_initializer,
                             use_bias=False, padding='SAME', name='conv1', reuse=reuse)
    bn1 = tf.layers.batch_normalization(conv1, training=is_training, name='bn1', reuse=reuse)
    relu1 = tf.nn.relu(bn1)
    # 14*14*64

    conv2 = tf.layers.conv2d(relu1, 128, (3, 3), strides=(2, 2), kernel_initializer=kernel_initializer,
                             use_bias=False, padding='SAME', name='conv2', reuse=reuse)
    bn2 = tf.layers.batch_normalization(conv2, training=is_training, name='bn2', reuse=reuse)
    relu2 = tf.nn.relu(bn2)
    # 7*7*128

    x3 = inception(relu2, 1, [64, 128, 32, 32], stage=3, is_training=is_training, reuse=reuse,
                   kernel_initializer=kernel_initializer)
    x4 = inception(x3, 1, [128, 192, 96, 64], stage=4, is_training=is_training, reuse=reuse,
                   kernel_initializer=kernel_initializer)
    x5 = inception(x4, 1, [192, 208, 48, 64], stage=5, is_training=is_training, reuse=reuse,
                   kernel_initializer=kernel_initializer)
    x6 = inception(x5, 1, [160, 224, 64, 64], stage=6, is_training=is_training, reuse=reuse,
                   kernel_initializer=kernel_initializer)
    # print('before gap: ', x4)
    x_mean = tf.reduce_mean(x6, [1, 2])

    # print('after gap: ', x4)
    # flatten = tf.contrib.layers.flatten(x4)
    # prob = tf.layers.dense(x4, 100, reuse=reuse, kernel_initializer=tf.contrib.layers.xavier_initializer())
    # prob = tf.layers.batch_normalization(prob, training=is_training, name='fbn', reuse=reuse)
    # print('prob', prob)

    return x_mean


# 训练
flatten = googlenet(xs, is_training=True, pooling_and_fc=True, reuse=False,
                    kernel_initializer=tf.contrib.layers.variance_scaling_initializer())
# 这里的操作，和之前没有任何的区别，那么我们在测试的时候，需要另一个网络，即全部都是false的，对吧

# 测试
flatten_test = googlenet(xs, is_training=False, pooling_and_fc=True, reuse=True,
                         kernel_initializer=tf.contrib.layers.variance_scaling_initializer())
# 这里必须注意，由于这里的计算图和前面的是一样的，直接运行会报错，我们需要做一个引用，即将里面带有参数的层的reuse属性设置为True
# 这里调用的两个一模一样的函数去构建计算图，这里如果不让第二个的所有命名层都reuse=True，那么就会报错

y = tf.layers.dense(flatten, 10, activation=tf.nn.softmax, name='fc')
y_test = tf.layers.dense(flatten, 10, activation=tf.nn.softmax, reuse=True, name='fc')
# 这里一定要注意，这里同样也需要reuse，为了让tf更方便找到需要reuse的是上面的这个函数，我们需要给上面的这个函数命个名！

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=ys_one_hot))

train = tf.train.AdamOptimizer(learning_rate).minimize(loss)

acc = tf.reduce_sum(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(ys_one_hot, 1)), tf.float32)) #argmax(y,1)按行找
acc_test = tf.reduce_sum(tf.cast(tf.equal(tf.argmax(y_test, 1), tf.argmax(ys, 1)), tf.float32))
# 到这一步位为止，其实我们搭建了两个不同配置，但是【共享】一套参数的计算图，我们就可以来进行测试了
# 然后你看，这一步的acc, 是由y和ys一起计算出来的，而y使用的是训练网络，这里我们需要让y变成测试网络

batch_size = 256
lr = 0.001

def parse_function(example_proto):
    features = {'image_raw': tf.FixedLenFeature([], tf.string),
                'label': tf.FixedLenFeature([], tf.int64)}
    features = tf.parse_single_example(example_proto, features)
    img = tf.decode_raw(features['image_raw'], tf.float32)
    img = tf.reshape(img, shape=(28, 28, 1))
    label = tf.cast(features['label'], tf.int64)
    return img, label

dataset = tf.data.TFRecordDataset('./mnist_train_records')
dataset = dataset.map(parse_function)
dataset = dataset.shuffle(buffer_size=50000)
dataset = dataset.batch(batch_size)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()#得到next_element这个tensor

'''首先用tf.global_variables得到所有的参数
然后根据参数的shape做乘法，得到每个参数的数据量
然后把每个参数的数据量求和，得到总参数量
vars = tf.global_variables()
tot_params = 0
for each_var in vars:
    print(each_var)
    shape = each_var.get_shape()
    variable_params = 1
    for dim in shape:
        variable_params *= dim.value
    print(variable_params)
    tot_params += variable_params   # ok，这个计算图的参数量大概就是141W，然后可以用我之前教你的方法估算一下存储的容量。
print('total params: ', tot_params)'''


config = tf.ConfigProto()
config.allow_soft_placement = True
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
sess.run(tf.global_variables_initializer())
sess.run(iterator.initializer)

import time
start_time = time.time() #计算运行时间
counter = 0
while True:
    try:
        #batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs, batch_ys = sess.run(next_element)
        _, acc_val = sess.run([train, acc], feed_dict={xs: batch_xs, ys: batch_ys, learning_rate: lr})

        if counter % 100 == 0:
            print(counter, acc_val / batch_size)
        if counter % 1000 == 0:
            lr = lr * 0.1
        if counter >= 2000:
            break
    except tf.errors.OutOfRangeError:
        # print('epoch over.')
        sess.run(iterator.initializer)
    counter += 1
end_time = time.time() # 51s
print ('train time: ', end_time - start_time)
