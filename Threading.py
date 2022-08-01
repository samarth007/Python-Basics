from threading import Thread,Lock
import time

db_value=1

def increase(lock):
  global db_value
  
  lock.acquire()
  local_val=db_value
  local_val+=1
  time.sleep(0.1)
  db_value=local_val
  lock.release()

if __name__== "__main__":
    print('Start value',db_value)
    lock=Lock()
    t1=Thread(target=increase,args=(lock,))
    t2=Thread(target=increase,args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value',db_value)