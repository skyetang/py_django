from django.shortcuts import render
from form_account.forms import LoginForm, RegForm, UserChangeForm
# Create your views here.


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            valid_data = form.cleaned_data
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {
        'form': form
    })


def reg_form(request):
    if request.method == 'POST':
        post_data = request.POST
        form = RegForm(data=post_data, files=request.FILES)
        if form.is_valid():
            valid_data = form.cleaned_data
            print(valid_data)
        else:
            print(form.errors)
    else:
        init_data = {
            'sex': 0,
            'email': 'test@163.com'
        }
        form = RegForm(initial=init_data)
    return render(request, 'reg_form.html', {
        'form': form
    })


def user_change_form(request):
    if request.method == 'POST':
        post_data = request.POST
        form = UserChangeForm(data=post_data, files=request.FILES)
        if form.is_valid():
            print('表单验证通过')
            valid_data = form.cleaned_data
            form.save()
        else:
            print(form.errors)
    else:
        form = UserChangeForm()
    return render(request, 'user_change_form.html', {
        'form': form
    })
