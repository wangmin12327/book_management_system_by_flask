#函数引用

# def show():
#     m = 100
#     print(m)
#     print("Show Run...")
# show()
# display = show  #函数结果赋给标识符，所以不能带（）
# display()
#闭包：一个嵌套函数内部访问外部函数中定义的函数
#外函数
# def out_func():
#     m = 100
#     #内函数
#     def in_func():
#         print("这是内函数的输出，引用了外函数的变量m，值为：",m)
#     return in_func



#使用闭包

# func1 = out_func()
# func2 = out_func()
# print("Hello")   #测试闭包延迟
# func1()
# func2()

#关键字：nonlocal
# def out_func():
#     out_n = 100
#     #内函数
#     def inner_func():
#         nonlocal out_n
#         out_n = 200   #关键字，加上可以用来修改函数外部变量的值
#         print("inner：",out_n)
#     print("out1:",out_n)
#     inner_func()
#     print("out2:", out_n)
#     return inner_func()
#
# if __name__ == '__main__':
#     of1 = out_func
#     of1()

#装饰器：在不修改原有函数定义和调用的情况下添加额外的功能，本质上是一个闭包函数
#特点：1.不修改已有函数的源代码
#     2.不修改已有函数的调用方式
#     3.给已有函数增加额外的功能
import time
def count_time(func):
    def inner():
        start = time.time()
        func()
        stop = time.time()
        print(f"函数共运行了{stop-start}秒")
    return inner

@count_time   #相当于把show当成func丢给上面的count_time函数执行
def show():
    s = 0
    for i in range(1000001):
        s += i
    print(s)
show()
#通用装饰器能适配所有带参的被装饰函数
#带参的装饰器

