import time, os


class MyTools:
    # 获取函数运行的时间,装饰器
    @staticmethod
    def get_running_time(func):
        def wraper(*args, **kwargs):
            start_time = time.time()
            s = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数执行时间为：{end_time - start_time:.2f}秒")
            return s

        return wraper

    # 拷贝单个文件
    @staticmethod
    def copy_file(old_file, new_file):
        with open(old_file, 'rb') as f1, open(new_file, 'wb') as f2:
            while True:
                data = f1.read(1024 * 1024)
                if not data:
                    break
                f2.write(data)

    # 拷贝整个目录(包括目录下所有子目录及文件)
    @staticmethod
    def copy_dir_all_files(old_dir, new_dir):
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        for dir in os.listdir(old_dir):
            old_path=old_dir+"/"+dir
            if os.path.isfile(old_path):
                MyTools.copy_file(old_path, new_dir + '/' + dir)
            elif os.path.isdir(old_path):
                MyTools.copy_dir_all_files(old_path, new_dir + "/" + dir)
