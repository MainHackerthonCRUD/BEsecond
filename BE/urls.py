"""
URL configuration for BE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from board.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('dj/', include('dj_rest_auth.urls')),
    path('dj/registration/', include('dj_rest_auth.registration.urls')),

    path('accounts/',include('allauth.urls')),

    # path('/kakao/',)

    # -------kakao---------
    path('kakao/callback/',kakako_callback),
    path('kakao/',kakao),
    # path('test/',test),








]
'''
{
    "username":"honggyu",
    "password1":"asdf1234qwer",
    "password2":"asdf1234qwer",
    "nickname":"hongddd"
}

{
    "title":"hello2",
    "body":"sdfs",
    "star":3
}
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMzYxODM5LCJpYXQiOjE3MjIzNTgyMzksImp0aSI6ImUwOWNiYmU0ZjRjZjQ1ZWU5NTFiZDM2MjllNDMwOWZiIiwidXNlcl9pZCI6N30.WCrE2bVKaw6XPV4avdKMN1sdvzP4BS54yMd7vyz9YV8



'''





'''
db에서 모델 객체 삭제하기
$ python manage.py shell
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from member.models import CustomUser
>>> CustomUser.objects.all().delete()
'''

'''
view에서 nickname=honggyuddd 조건으로 mypage 반환하게 해놨음
id 기준으로 할 지, 다른 조건으로 할 지 생각해봐야 함

'''