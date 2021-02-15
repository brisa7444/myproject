from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
import pymysql
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

#连接数据库
conn = pymysql.connect(host='47.104.70.37', port=3306, user='root', passwd='bytedance', db='bytedance',
                       charset='utf8')
cursor = conn.cursor()



def WAFLogin(request):
    if (request.method == 'POST'):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            # Redirect to a success page.
            return redirect('firewall:index')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("username or password is incorrect")

    return render(request, 'firewall/login.html')

@login_required
def index(request):
    sql = cursor.execute("select * from attackLog")
    results = cursor.fetchall()
    return render(request, 'firewall/index.html')

def logShow(request):
    if(request.method=='POST'):
        choice=request.POST.get("type")

    sql = "select * from %s"
    cursor.execute(sql,choice)
    results = cursor.fetchall()

def blacklistShow(request):
    sql = cursor.execute("select * from blacklist")
    results = cursor.fetchall()

def whitelistShow(request):
    sql = cursor.execute("select * from whitelist")
    results = cursor.fetchall()

def searchWaiting(request):
    if(request.method=='POST'):
        choice=request.POST.get("type")
        keyword=request.POST.get("keyword")

        # 执行SQL，模糊查询
        sql = "select * from %s where attackType like '%%s%'"
        cursor.execute(sql,(choice,keyword))
        results = cursor.fetchall()


def ruleChange(request):
    if (request.method == 'POST'):
        rule=request.POST.get("rule")

        sql = cursor.execute("select * from rule where vulnerable like '%%s%'")
        results = cursor.fetchall()

        for result in results:
            sql="update rule set status=1 where id=%s"
            cursor.execute(sql,result[0])
            conn.commit()
    return HttpResponse("hello world!")









