import os.path
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
import json

# Create your views here.


def hello_world(request):
    return HttpResponse('hello world')


def hello_china(request):
    return HttpResponse('hello china')


def hello_html(request):
    html = '''
        <html>
            <body>
                <h1 style="color:red">hell_html</h1>
            </body>
        </html>
    '''
    return HttpResponse(html)


def article_list(request, month):
    return HttpResponse('article is :{}'.format(month))


def search(request):
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功：{}'.format(name))


def render_html(request):
    return render(request, 'render_html.html')


def request_info(request):
    method = request.method
    print(method)
    # 封装好的简化后的请求头信息
    print(request.headers)
    # 获取user-agent的两种方式
    agent = request.META.get('HTTP_USER_AGENT', None)
    print(agent)
    print(request.headers['user-agent'])
    print(request.GET.get('name', None))
    return HttpResponse(request.headers)


def response(request):

    # 更改状态码
    res = HttpResponse('响应了', status='201')
    print(res.status_code)
    res.status_code = 204
    res['TOKEN'] = 'abc123'
    return res


def json_response(request):
    info = {
        'name': 'skye',
        'age': '22',
        'sex': 'man'
    }
    return JsonResponse(info)


def file_response(request):
    p = os.path.dirname(__file__)
    print(p)
    file = open('static/2.jpg', 'rb')
    return FileResponse(file)


def not_found(request):
    return HttpResponse('数据未找到，404')


def find_page(request, article_id):
    if article_id < 1000:
        # return HttpResponseRedirect('/hello/not/found')
        # return HttpResponseRedirect(reverse('not_found'))
        return redirect('not_found')
    return HttpResponse('{}查到了'.format(article_id))


class Cat(object):
    def display(self):
        return '一只小猫'

def index(request):
    username = 'skye'
    age = 25

    list = [{
        'name': '张三',
        'age': 25
    }, {
       'name': '李四',
       'age': 26
    }]

    cat = Cat()
    return render(request, 'index.html', {
        'username': username,
        'age': age,
        'list': list,
        'cat': cat
    })


def tag(request):
    list = [
        {'name': '张三', 'age': 25},
        {'name': '李四', 'age': 26},
        {'name': '李四2', 'age': 26, 'sex': 'man'},
        {'name': '李四34', 'age': 26}
    ]
    # list = []
    return render(request, 'tag.html', {
        'list': list
    })


def extend(request):
    return render(request, 'extend.html')

