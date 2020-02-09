# 最简单的resnet18
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

tf.reset_default_graph()  # 防止存在already exit问题
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

xs = tf.placeholder(tf.float32, [None, 28, 28, 1])  # 28x28 mnist.train.images:[None]*784
ys = tf.placeholder(tf.float32, [None, 10])  # 10类 mnist.train.labels:[None]*10
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
# 非常奇妙啊，这个问题可能是缓存导致的

# 测试
flatten_test = googlenet(xs, is_training=False, pooling_and_fc=True, reuse=True,
                         kernel_initializer=tf.contrib.layers.variance_scaling_initializer())
# 这里必须注意，由于这里的计算图和前面的是一样的，直接运行会报错，我们需要做一个引用，即将里面带有参数的层的reuse属性设置为True
# 这里调用的两个一模一样的函数去构建计算图，这里如果不让第二个的所有命名层都reuse=True，那么就会报错

y = tf.layers.dense(flatten, 10, activation=tf.nn.softmax, name='fc')
y_test = tf.layers.dense(flatten, 10, activation=tf.nn.softmax, reuse=True, name='fc')
# 这里一定要注意，这里同样也需要reuse，为了让tf更方便找到需要reuse的是上面的这个函数，我们需要给上面的这个函数命个名！

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=ys))

train = tf.train.AdamOptimizer(learning_rate).minimize(loss)

acc = tf.reduce_sum(tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(ys, 1)), tf.float32)) #argmax(y,1)按行找
acc_test = tf.reduce_sum(tf.cast(tf.equal(tf.argmax(y_test, 1), tf.argmax(ys, 1)), tf.float32))
# 到这一步位为止，其实我们搭建了两个不同配置，但是【共享】一套参数的计算图，我们就可以来进行测试了
# 然后你看，这一步的acc, 是由y和ys一起计算出来的，而y使用的是训练网络，这里我们需要让y变成测试网络

sess = tf.Session()
sess.run(tf.global_variables_initializer())

batch_size = 512
lr = 0.001
import time
start_time = time.time()
for i in range(2000):
    if i % 1000 == 0:
        lr = lr * 0.1
    batch_xs, batch_ys = mnist.train.next_batch(batch_size)
    # 这里的batch_xs，里面的每个元素 应该都是784长度的向量，你需要转化为28 28 1, 现在再来看效果如何
    batch_xs = batch_xs.reshape(batch_size, 28, 28, 1)

    _, acc_val = sess.run([train, acc], feed_dict={xs: batch_xs, ys: batch_ys, learning_rate: lr})

    if i % 100 == 0:
        print(i, acc_val / batch_size)

end_time = time.time()
print('train time', end_time - start_time)
    # 接下来是测试
true_presicions = 0
for i in range(100):
    true_presicions += sess.run(acc_test,
                                feed_dict={xs: mnist.test.images[100 * i:100 * (i + 1)].reshape(100, 28, 28, 1),
                                           ys: mnist.test.labels[100 * i:100 * (i + 1)]})
print('final result:', true_presicions / 10000)