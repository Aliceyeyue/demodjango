from django.shortcuts import render,render_to_response,HttpResponse
from Foods.models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect
def add_food_type(request):
    type_list = ["经典牛排", "意面/烩饭", "风味披萨", "甜品小食", "酒水饮料", "其他"]
    for types in type_list:
        t = Foods_type()
        t.label = types
        t.description = "%s 好吃不贵" % types
        # t.save()
    return HttpResponse("类型保存成功")
    # 添加商品
import random
import json
def add_food(request):
    food_list = ["茶漱海鲜汤","玉米海螺沟","芝士蛋糕卷","芝士大虾","西冷牛排","草莓布丁杯","黑椒牛排","西红柿炒鸡蛋"]
    for food in food_list:
        t=Foods()
        t.name = food
        t.price = random.randint(1,200)
        t.picture = '1.jpg'
        t.description = '%s 美味大餐'% food
        t.type_id = Foods_type.objects.get(id = random.randint(1,6))
        # t.save()
    return HttpResponse('食品保存成功')
def add_news(request):
    address = ['石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番', '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯', '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏']
    for i in range(10):
        news = News()
        title = "贵族食代牛排%s餐厅开业"%random.choice(address)
        news.title = title
        news.time = "%s-%s-%s"%(
            random.randint(1000, 3000),
            random.randint(1, 12),
            random.randint(1, 28)
        )
        news.description = title*10
        news.image = "1.jpg"
        news.content = title*50
        news.type = "新闻资讯"
        #news.save()

    return HttpResponse("文章保存成功")

#添加文章
def add_shop(request):
    address = ['石河子', '阿拉尔市', '图木舒克', '五家渠', '哈密', '吐鲁番', '阿克苏', '喀什', '和田', '伊宁', '塔城', '阿勒泰', '奎屯', '博乐', '昌吉', '阜康', '库尔勒', '阿图什', '乌苏']
    for i in range(100):
        shop = Shop()
        shop.name = "贵族食代牛排%s餐厅"%random.choice(address)
        shop.picture = "1.jpg"
        shop.open_time = "上午10:00-11:00 下午15:30-17:00"
        shop.stop_car = "付费停车，30元/平米/小时/"
        shop.address = random.choice(address)
        shop.label = "法国菜,有包间,有车位,可刷卡,崇文区,地铁1号线,地铁2号线,地铁5号线,崇文门外大街,前门总医院,天坛,祈年殿,龙潭湖公园,北京体育馆,中央戏剧学院,崇文区儿童医院,新世界商场,北京站,新闻大厦,北京饭店,北京市政府,东交民巷,天安门,朋友聚会,家人就餐,谈情约会"
        shop.save()
        for i in range(random.randint(6,8)):
            shop.foods_id.add(
                Foods.objects.get(id = random.randint(1,8))
            )
            shop.save()

    return HttpResponse("店铺保存成功")


def ajax_get_page(request):
    return render_to_response(request,'ajax_get_page.html')

def ajax_get_data(request):
    html = '<span style="color:red;">牛</span>'
    shop_list = [{'name':shop.name.replace('牛',html)} for shop in Shop.objects.all()]
    return JsonResponse({'shop_list':shop_list})

def form_check(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            pass
        else:
            error='用户名密码不可以为空'
    return render(request,'form_check.html')

from Foods.forms import *
def p_form(request):
    userform = UserForm()
    foodform = FoodsForm()
    return render(request,'python_forms.html',locals())

import hashlib
def setCookie(request):
    # return render(request, 'index.html')

    # 创建一个响应
    response = render(request, 'index.html')
    # response.set_cookie()
    # 对响应实例设置cookie
    # 1.多条cookie多次设置
    # 2.cookie黎明不要有中文
    response.set_cookie('username', 'laobian')
    response.set_cookie('age', '18')
    # 返回携带cookie的响应
    return response
def xs(request,page):
    cookie_username = request.COOKIES.get('username')
    return render(request,'news.html',locals())
def del_cookie(request):
    response = render(request,'index.html')
    response.delete_cookie('username')
    return response
def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User()
        user.username=username
        user.password=set_password(password)
        user.save()
    return render(request,'register.html',locals())

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_username = request.COOKIES.get('username')
        session_username = request.session.get('username')
        if cookie_username and session_username and cookie_username == session_username:

            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner
@loginValid
def index(request):
    news_list = News.objects.order_by('-time')[:8]
    return render_to_response('index.html',locals())

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
    # 通过查询判断用户名是否存在
        user = User.objects.filter(username=username).first()
        if user:
        # 将请求携带的密码进行加密，进行比对
            post_password = set_password(password)
            if user.password == post_password:
            # 密码正确设置cookie
                response = HttpResponseRedirect("/index/")
                response.set_cookie("username", user.username)
                request.session["username"] = user.username
            # 返回响应
                return response
    return render(request, "login.html")

def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    del request.session['username']
    return response

from django.views import View
class FoodView(View):
    def __init__(self,**kwargs):
        super(FoodView,self).__init__()
        self.result = {
            'version':'v1.0',
            'code':200,
            'data':[]
        }
    def is_exit(self,id):
        try:
            data = Foods.objects.get(id=id)
        except Exception as e:
            self.result['code'] = 500
            self.result['data'].append(str(e))
            return False
        else:
            return data

    def one_data(self, data):
        d = {"name": data.name, "price": data.price, "picture": data.picture.url, "description": data.description,
             "type": data.type_id.label}
        self.result["data"].append(d)
    def get(self,request):
        '''
        查询
        '''
        id=request.GET.get('id')
        if id:
            try:
                data=Foods.objects.get(id=id)
            except Exception as e:
                self.result['code'] = 600
                self.result['data'].append(str(e))
            else:
                d = {'name':data.name,'price':data.price,'picture':data.picture.url,"description": data.description,"type": data.type_id.label}
                self.result['data'].append(d)
        else:
            data = [
                {"name": data.name, "price": data.price, "picture": data.picture.url, "description": data.description,
                 "type": data.type_id.label} for data in Foods.objects.all()]
            self.result["data"] = data
        return JsonResponse(self.result)

    def post(self,request):
        '''增加数据用
        '''
        post_data = request.POST
        name = post_data.get('name')
        price = post_data.get('price')
        picture = post_data.get('picture')
        description = post_data.get('description')
        type_id = post_data.get('type_id')

        foods = Foods()
        foods.name = name
        foods.price = price
        foods.picture = picture
        foods.description = description
        foods.type_id = Foods_type.objects.get(id=int(type_id))
        foods.save()
        return JsonResponse(self.result)

    def put(self,request):
        '''修改'''
        put_data = json.loads(request.body.decode())
        id = put_data.get("id")
        name = put_data.get("name")
        price = put_data.get("price")
        picture = put_data.get("picture")
        description = put_data.get("description")
        type_id = put_data.get("type_id")

        foods = self.is_exit(id)
        if foods:
            foods.name = name
            foods.price = price
            foods.picture = picture
            foods.description = description
            foods.type_id = Foods_type.objects.get(id=int(type_id))
            foods.save()
            self.one_data(foods)

        return JsonResponse(self.result)

    def delete(self, request):
        delete_data = json.loads(request.body.decode())
        id = delete_data.get("id")

        foods = self.is_exit(id)
        if foods:
            d = {
                "name": foods.name,
                "price": foods.price,
                "picture": foods.picture.url,
                "description": foods.description,
                "type": foods.type_id.label
            }
            self.result["data"].append(d)
            foods.delete()
        return JsonResponse(self.result)


def ajax_vue(request):
    return render(request,'ajax_vue.html')

def meishi(request):
    return render(request,'meishi.html')
# Create your views here.
