from tools.my_tools import MyTools
old_dir=("/home/tarena/PycharmProjects/tedu_execises/mysql_data")
new_dir=old_dir+"_备份"

MyTools.copy_dir_all_files(old_dir,new_dir)
