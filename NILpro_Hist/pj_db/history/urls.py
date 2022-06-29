from django.contrib import admin
from django.urls import path

from . import views
from .admin import mypage_site

app_name ="history"



urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    
    # <pk>にPostのIDを渡すと表示される。
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
    path('mypage/', mypage_site.urls),
    path('top/', views.top, name='top'),
]
