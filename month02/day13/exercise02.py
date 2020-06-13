'''
利用线程池拷贝一个目录下的所有文件
'''
from multiprocessing import Pool, Queue
from tools.my_tools import MyTools
import os


def get_dir_size(dir):
    return sum(list(map(lambda file: os.path.getsize(dir + "/" + file), os.listdir(dir))))


q = Queue()
old_dir = input("要拷贝的目录：")
new_dir = old_dir + "-备份"
total_size = get_dir_size(old_dir)
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

pool = Pool(4)
for file in os.listdir(old_dir):
    q.put(get_dir_size(new_dir))
    pool.apply_async(MyTools.copy_file(old_dir + "/" + file, new_dir + "/" + file))

content_size = 0
while content_size < total_size:
    content_size += q.get()
    print(f"完成进度：{content_size*100/total_size:.2f}%")
pool.close()
pool.join()
