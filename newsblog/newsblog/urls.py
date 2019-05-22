
from django.contrib import admin
from django.conf.urls import url,include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^blogs/',include('blogs.urls')),
    url(r'^$', views.home, name='home'),
    url('portfolio',views.portfolio,name='portfolio'),
    url('aboutme',views.aboutme,name='aboutme'),
    url('about',views.about,name='about'),
    url('contact',views.contact,name='contact'),
    url('news',views.news,name='news'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)