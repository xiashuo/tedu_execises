from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import hashlib

# Create your views here.
def reg_view(request):

    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #处理提交数据，创建用户
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 != password_2:
            return HttpResponse('The password is wrong')

        #检查账号是否已经存在
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('The username is already existed')

        #处理密码 - hash算法【散列】
        #算法特点
        #1, 不可逆     -密码存储
        #2, 输入不变 输出不变
        #3, 定长输出 【明文不同，算法恒定，则输出长度一定】
        #4，雪崩  -文件完整性校验  - BAT - 40G 下载完后如何计算hash值
        m = hashlib.md5()
        m.update(password_1.encode())
        password_h = m.hexdigest()

        try:
            user = User.objects.create(username=username, password=password_h)
        except Exception as e:
            print('--create error is %s'%(e))
            return HttpResponse('The username is already existed')

        #免登陆一天
        request.session['uid'] = user.id
        request.session['username'] = username

        return HttpResponse('--reg is ok')



def login_view(request):

    if request.method == 'GET':
        #如果用户已登录 显示  已登录
        #优先检查session
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('您已登录')
        #检查Cookies
        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        if username and uid:
            request.session['username'] = username
            request.session['uid'] = uid
            return HttpResponse('您已登录！')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        #处理数据
        username = request.POST['username']
        password = request.POST['password']

        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            print('--login get error %s'%(e))
            return HttpResponse('The username or password is wrong')

        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        if password_h != old_user.password:
            return HttpResponse('The username or password is wrong')

        #存储会话状态
        request.session['uid'] = old_user.id
        request.session['username'] = username

        #判断是否要存储Cookies
        resp = HttpResponse('login is ok')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24*3)
            resp.set_cookie('uid', old_user.id, 3600*24*3)
        return resp





















