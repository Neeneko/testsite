from django.conf.urls import url

from . import views

urlpatterns =   [
                    url(r'^login/', views.login, name='login'),
                    url(r'^logout/', views.logout, name='logout'),
                    url(r'^threads', views.threads, name='threads'),
                    url(r'^thread/view/(?P<thread_id>[0-9a-f-]+)/$', views.view_thread, name="view_thread"), 
                    url(r'^comment/create/(?P<thread_id>[0-9a-f-]+)/$', views.create_comment, name="create_comment"), 
                    url(r'^thread/delete/(?P<thread_id>[0-9a-f-]+)/$', views.delete_thread, name="delete_thread"), 
                    url(r'^thread/create/', views.create_thread, name="create_thread"), 
                    url(r'^authors', views.authors, name='authors'),
                    url(r'^author/delete/(?P<author_id>[0-9a-f-]+)/$', views.delete_author, name="delete_author"), 
                    url(r'^$', views.index, name='index'),
                ]
