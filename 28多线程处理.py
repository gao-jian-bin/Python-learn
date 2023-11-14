import time
import threading

# 创建互斥锁
output_lock = threading.Lock()


def sing(mes):
    while 1:
        with output_lock:
            print(mes)
            time.sleep(1)


def dance(meg):
    while 1:
        with output_lock:
            print(meg)
            time.sleep(1)


def rap(mes):
    while 1:
        with output_lock:
            print(mes)
            time.sleep(1)


if __name__ == '__main__':
    # sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance, args=('dance',))
    sing_thread = threading.Thread(target=sing, args=('singing',))
    rap_thread = threading.Thread(target=rap, kwargs={'mes': 'raping'})

    sing_thread.start()
    dance_thread.start()
    rap_thread.start()

#     sing_thread.join()
#     dance_thread.join()
#     rap_thread.join()
# # import threading

# 定义一个函数，作为线程的执行体
# def my_function():
#     print("This is my thread.")
#
# # 创建一个线程
# my_thread = threading.Thread(target=my_function)
#
# # 启动线程
# my_thread.start()
#
# # 在主线程中调用join()方法，等待my_thread执行完成
# my_thread.join()
#
# # 主线程会等待my_thread执行完成后再继续执行下面的代码
# print("Thread execution is complete.")
