from django.shortcuts import render_to_response,HttpResponse
from Foods.models import *

def index(request):
    return render_to_response('index.html',locals())
def shop(request):
    shop_list = Shop.objects.all()
    return render_to_response('shop.html',locals())

from django.shortcuts import render
def tr(request):
    #接受数据
    food_type_list = Foods_type.objects.all()

    if request.method=='POST':
        args = request.POST
        name = args.get('name')
        price = args.get('price')
        description = args.get('description')
        #
        # #picture = args.get('picture')#不对，这个文件类型不能这么获取
        picture = request.FILES.get('picture')
        type_id = args.get('type_id')
    #保存数据
        food = Foods()
        food.name = name
        food.price = price
        food.picture = picture
        food.description = description
        food.type_id = Foods_type.objects.get(id=int(type_id))
        food.save()
    return render(request,'test_request.html',locals())