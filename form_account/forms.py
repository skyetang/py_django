import re
from account.models import User
from django import forms
from django.shortcuts import render


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, required=False, help_text='[手机号]')
    password = forms.CharField(label='密码', max_length=30, min_length=6, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, username):
            raise forms.ValidationError('请输入手机号')
        return username

    # 重新clean方法，来重置整个校验方法
    def clean(self):
        # 通过父类的clean方法返回数据
        data = super().clean()
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # 查询用户名和密码匹配的用户
            user_list = User.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('用户名不存在')
            # TODO 一般是会使用加密算法进行验证
            if not user_list.filter(password=password).exists():
                raise forms.ValidationError('密码不正确')
        return data


class RegForm(forms.Form):
    SEX_CHOICE = (
        (1, '男'),
        (0, '女')
    )
    username = forms.CharField(label='用户名', max_length=100, required=False, help_text='手机号')
    password = forms.CharField(label='密码', max_length=30, min_length=6, widget=forms.PasswordInput)
    email = forms.EmailField(label='电子邮件', max_length=100)
    sex = forms.ChoiceField(label='用户性别', choices=SEX_CHOICE, initial=0, widget=forms.RadioSelect)


# 通过模型创建表单，进行基础信息修改
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname', 'avatar')
        widgets = {
            'password': forms.PasswordInput(attrs={
                'style': 'border 1px red'
            })
        }
        labels = {
            'username': '手机号'
        },
        error_messages = {
            'username': {
                'max_length': '用户名超过了最大长度'
            },
            'password': {
                'min_length': '密码最短要6位数'
            }
        }



