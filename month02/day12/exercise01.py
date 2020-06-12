from multiprocessing import Process
import os
file_path=input("file_path >>")
file_size = os.path.getsize(file_path)


def write(content, file):
    with open(file, "wb") as f:
        f.write(content)


with open(file_path, "rb") as f:
    content1 = f.read(file_size//2)
    content2 = f.read()
    p1 = Process(target=write, args=(content1, "top_"+file_path))
    p2 = Process(target=write, args=(content2, "bottom_"+file_path))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
