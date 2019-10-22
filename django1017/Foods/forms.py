from django import forms
from django.forms import ModelForm
from Foods.models import Foods

class UserForm(forms.Form):
    username = forms.CharField(max_length=12,min_length=6)
    password = forms.CharField(
        max_length=12,
        min_length=6,
        widget = forms.PasswordInput(attrs={'class':'title'}),
        required=True,
        label='密码',
        error_messages={'required':'密码不可以为空'}

    )

class FoodsForm(ModelForm):
    class Meta:
        model=Foods
        # fields = '__all__'
        fields = ('name','price','picture','description')
        labels={
            'name':'食品名称',
            'price':'食品价格',
            'picture':'食品图片',
            'description':'食品描述',
        }
    def clean_name(self):
        '''
        校验的名称必须是clean_字段名称
        :return:
        '''
        pool = ['admin','aaa']
        name = self.cleaned_data.get('name')
        if name in pool:
            pass