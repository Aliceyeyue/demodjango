from django.http import HttpResponse

#加载模板
from django.template.loader import get_template
#加载并渲染
from django.shortcuts import render_to_response

def index_page(request):
    navigation = ['ds首页','新闻中心','产品展示','成功案例',
                  '在线留言','联系我们','资质荣誉']
    slide = [
        'banner.jpg','banner2.jpg','banner.jpg','banner2.jpg',
    ]
    imgs = [
        {'href':'','src':'dianzi.png'},
        {'href':'','src':'team.png'},
        {'href':'','src':'case.png'},
        {'href':'','src':'kefu.png'},
    ]
    room_type = [
        {'name':'客厅','src':'/static/images/round1.jpg'},
        {'name':'卧室','src':'/static/images/round2.jpg'},
        {'name':'餐厅','src':'/static/images/round3.jpg'},
        {'name':'厨房','src':'/static/images/round4.jpg'},
        {'name':'卫生间','src':'/static/images/round5.jpg'},
        {'name':'阳台','src':'/static/images/round6.jpg'},
        {'name':'背景墙','src':'/static/images/round7.jpg'},
        {'name':'吊顶','src':'/static/images/round8.jpg'},
    ]
    cases = [
        {'href':'','case_name':'一居室装修'},
        {'href':'','case_name':'三居室装修'},
        {'href':'','case_name':'别墅装修'},
        {'href':'','case_name':'四合院装修'},
        {'href':'','case_name':'酒吧装修'},
        {'href':'','case_name':'饭店装修'},
        {'href':'','case_name':'服装店装修'},
        {'href':'','case_name':'数码城装修'}
    ]
    pics = [
        {'name':'效果图1','src':'/static/images/pic7.jpg'},
        {'name':'效果图2','src':'/static/images/pic8.jpg'},
        {'name':'效果图3','src':'/static/images/pic3.jpg'},
        {'name':'效果图4','src':'/static/images/pic4.jpg'},
        {'name':'效果图5','src':'/static/images/pic5.jpg'},
        {'name':'效果图6','src':'/static/images/pic6.jpg'},
    ]
    return render_to_response('index.html', locals())