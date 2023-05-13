# 实现数据可视化中的数据平滑
import numpy as np
import matplotlib.pylab as plt
 
'''
其它的一些知识点：
raise：当程序发生错误，python将自动引发异常，也可以通过raise显示的引发异常
一旦执行了raise语句，raise语句后面的语句将不能执行
'''
 
def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re
 
def LabberRing():
    t = np.linspace(-4, 4, 100)   # np.linspace 等差数列,从-4到4生成100个数
    print('t=', t)
 # np.random.randn 标准正态分布的随机数，np.random.rand 随机样本数值
    y = np.sin(t) + np.random.randn(len(t)) * 0.1   # 标准正态分布中返回1个，或者多个样本值
    print('y=', y)
    
    plt.plot(t, y, '--k')     # plot(横坐标，纵坐标， 颜色)
    
    y_av = moving_average(y, 10)
    plt.plot(t, y_av, 'k')
    plt.xlabel('x')
    plt.ylabel('Value')
    # plt.grid()网格线设置
    plt.grid(True)
    plt.show()
    return
 
LabberRing()  # 调用函数
