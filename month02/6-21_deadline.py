'''
6、用代码展示基于SQLAIchemy的CRUD。

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(
    "mysql+pymysql://root:135456..@localhost:3306/sqlalchemy_test",
    echo=True
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    email = Column(String(64))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"(id:{self.id},name:{self.name},email:{self.email})"


# 创建表
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session=Session()

# 增加1条数据
# obj=User(name="张三",email="zhangsan@qq.com")
# session.add(obj)

# 增加多条数据
# list_users=[
#     User("李四","lisi@qq.com"),
#     User("李五","liwu@qq.com"),
#     User("李六","liliu@qq.com"),
#     User("李七","liqi@qq.com"),
#     User("李八","liba@qq.com")
# ]
# session.add_all(list_users)

# 删除数据
# session.query(User).filter(User.id == 6).delete()

# 修改数据
# session.query(User).filter_by(id=5).update({"name":"xiashuobad","email":"654017381@qq.com"})
# session.commit()

# 查找数据
# 查询所有数据
sql=session.query(User) # 查询生成的sql代码
print(sql)
ret=sql.all() # 返回的是User对象的列表
print(ret)
# 只显示第一行
ret=sql.first()
print(ret)
# 查询某几个字段的数据
ret=session.query(User.name).all()
print(ret)
# 条件查找
ret=session.query(User).filter_by(name="xiashuobad").all()
print(ret)
ret=session.query(User).filter(User.id.in_([1,2,3])).all() #查询id在1,2,3中的数据
print(ret)
ret=session.query(User).filter(~User.id.in_([1,2,3])).all() #查询id不在1,2,3中的数据，~表示非
print(ret)
'''


# 7、用python程序实现冒泡排序。
def bubble_sort(list_target):
    for i in range(len(list_target) - 1, 0, -1):
        for j in range(i):
            if list_target[j] > list_target[j + 1]:
                list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]


# 8、用python程序实现插入排序。
def insert_sort(list_target):
    for i in range(1, len(list_target)):
        current_val = list_target[i]
        p = i
        while p > 0 and current_val < list_target[p - 1]:
            list_target[p] = list_target[p - 1]
            p -= 1
        list_target[p] = current_val


# 9、用python程序实现选择排序。
def selection_sort(list_target):
    for i in range(len(list_target) - 1):
        min_index = i
        for j in range(i + 1, len(list_target)):
            if list_target[j] < list_target[i]:
                min_index = j
        list_target[min_index], list_target[i] = list_target[i], list_target[min_index]


# 10、用python程序实现希尔排序。
def shell_sort(list_target):
    gap = len(list_target) // 2
    while gap > 0:
        for i in range(gap):
            gap_insert_sort(list_target, i, gap)
        gap = gap // 2


def gap_insert_sort(list_target, start, gap):
    for i in range(start + gap, len(list_target), gap):
        temp = list_target[i]
        j = i
        while j > start and temp < list_target[j - gap]:
            list_target[j] = list_target[j - gap]
            j -= gap
        list_target[j] = temp


# 11、用python程序实现归并排序。
def merge_sort(list_target):
    if len(list_target) == 1:
        return
    mid = len(list_target) // 2
    left_half = list_target[:mid]
    right_half = list_target[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    list_target[:] = merge_ordered_list(left_half, right_half)


def merge_ordered_list(left_half, right_half):
    list_merge = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            list_merge.append(left_half[i])
            i += 1
        else:
            list_merge.append(right_half[j])
            j += 1

    while i < len(left_half):
        list_merge.append(left_half[i])
        i += 1
    while j < len(right_half):
        list_merge.append(right_half[j])
        j += 1
    return list_merge


# 12、用python程序实现快速排序。
def partition(list_target, first, last):
    bub_value = list_target[first]
    i, j = first + 1, last
    while True:
        while i <= j and list_target[i] <= bub_value:
            i += 1
        while i <= j and list_target[j] >= bub_value:
            j -= 1
        if i > j:
            break
        list_target[i], list_target[j] = list_target[j], list_target[i]
    list_target[first], list_target[j] = list_target[j], list_target[first]
    return j


def quick_sort_helper(list_target, first, last):
    if first < last:
        # split_point = partition(list_target, first, last)
        bub_value = list_target[first]
        i, j = first + 1, last
        while True:
            while i <= j and list_target[i] <= bub_value:
                i += 1
            while i <= j and list_target[j] >= bub_value:
                j -= 1
            if i > j:
                break
            list_target[i], list_target[j] = list_target[j], list_target[i]
        list_target[first], list_target[j] = list_target[j], list_target[first]
        quick_sort_helper(list_target, first, j - 1)
        quick_sort_helper(list_target, j + 1, last)


def quick_sort(list_target):
    quick_sort_helper(list_target, 0, len(list_target) - 1)


# 13、用python程序实现堆排序。
def heap_adjust(list_target, s, m):
    temp = list_target[s - 1]
    i = 2 * s
    while i <= m:
        if i < m and list_target[i - 1] < list_target[i]:
            i += 1
        if list_target[i - 1] <= temp:
            break
        list_target[s - 1] = list_target[i - 1]
        s = i
        i *= 2
    list_target[s - 1] = temp


def heap_sort(list_target):
    lenth = len(list_target)
    for i in range(lenth // 2, 0, -1):
        heap_adjust(list_target, i, lenth)

    for j in range(lenth, 1, -1):
        list_target[j - 1], list_target[0] = list_target[0], list_target[j - 1]
        heap_adjust(list_target, 1, j - 1)


# 14、用python程序实现桶排序。
# 桶的个数为：(maxnum-mininum)//len(list_target)+1
# 映射规则为：index=(x-mininum)//len(list_target)
def bucketSort(list_target):
    maxinum, mininum = max(list_target), min(list_target)
    length = len(list_target)
    bucket_arr = [[] for i in range((maxinum - mininum) // length + 1)]
    for i in list_target:
        index = (i - mininum) // length
        bucket_arr[index].append(i)
    list_target.clear()
    for bucket in bucket_arr:
        bucket.sort()
        list_target.extend(bucket)


# 15、用python程序实现基数排序。
# 从右边起（个、十、百、。。。），获取数字的第i位
def get_digit_i(number, i):
    num_str = str(number)
    if i > len(num_str):
        return 0
    else:
        return int(num_str[-i])


def radix_sort(list_target):
    bucket_arr = [[] for _ in range(10)]
    # 获取最大值的长度，即一共有多少位数，则后面就需要循环操作几次
    length = len(str(max(list_target)))
    # 从右边开始，按照个位、十位、百位。。。的顺序进行循环操作。
    for i in range(1, length + 1):
        # 根据当前位数，将所有数字放入相应的桶中。
        for val in list_target:
            index = get_digit_i(val, i)
            bucket_arr[index].append(val)
        # 放所有数据按照顺序从桶中取出来放到list_target中
        list_target.clear()
        for bucket in bucket_arr:
            list_target.extend(bucket)
        # 清空所有桶
        for bucket in bucket_arr:
            bucket.clear()


if __name__ == '__main__':
    list_target = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubble_sort(list_target)
    # selection_sort(list_target)
    # insert_sort(list_target)
    # shell_sort(list_target)
    # merge_sort(list_target)
    quick_sort(list_target)
    # heap_sort(list_target)
    # bubble_sort(list_target)
    # radix_sort(list_target)
    print(list_target)

