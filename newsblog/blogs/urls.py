
from django.conf.urls import url
from.import views


urlpatterns = [
   url(r'^$',views.blog,name="list"),
   url(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name="detail"),  
]
