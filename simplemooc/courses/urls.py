from django.conf.urls import  include, url
from simplemooc.courses.views import courses, details, enrollment, announcements
 
urlpatterns = [
    url(r'^$', courses, name='courses'),
   # url(r'^(?P<slug>[-\w]+)/$', details, name='details'),
    url(r'^(?P<slug>[-\w]+)/$', details, name='details'),
    url(r'^(?P<slug>[-\w]+)/inscricao/$', enrollment, name='enrollment'),
    #url(r'^(?P<pk>\d+)/$', details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', announcements, name='announcements')

]