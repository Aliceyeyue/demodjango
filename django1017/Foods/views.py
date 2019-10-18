from django.shortcuts import render_to_response,HttpResponse
from Foods.models import *

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












# Create your views here.
