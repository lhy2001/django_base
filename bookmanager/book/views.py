from django.shortcuts import render

# Create your views here.
"""
视图函数有两个要求
1.视图函数第一个参数就是接收请求
2.必须返回一个响应"""
from django.http import HttpResponse
from django.http import HttpRequest
def index(request):
    # render(请求，模板名字)
    context = {
        'name':'马上双11，点击有惊喜'
    }
    return render(request,'book/index.html',context=context)