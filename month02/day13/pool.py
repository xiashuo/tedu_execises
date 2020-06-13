from multiprocessing import Pool
import time,random
def worker(msg,sec):
    time.sleep(sec)
    print(time.ctime(),"---",msg)
pool=Pool(4)

for i in range(10):
    msg=f"worker{i}"
    pool.apply_async(func=worker,args=(msg,random.randint(1,5)))

pool.close()

pool.join()


