from multiprocessing import Process, Value,Lock
import time

def add_numb(num,lock):
    lock.acquire()
    for i in range(100):
        time.sleep(0.01)
        num.value+=1
    lock.release()

if __name__ == '__main__':
    lock=Lock()
    Initial_num=Value('i',0)
    print('Initial value was',Initial_num.value)

    p1=Process(target=add_numb,args=(Initial_num,lock))
    p2=Process(target=add_numb,args=(Initial_num,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Final value is ', Initial_num.value)