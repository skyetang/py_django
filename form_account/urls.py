from django.urls import path
from form_account.views import login_form, reg_form, user_change_form


urlpatterns = [
    path('login/', login_form, name='login_form'),
    path('reg/', reg_form, name='reg_form'),
    path('user/change/', user_change_form, name='user_change_form')
]
