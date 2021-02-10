from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('viewname', view_name, name='viewname'),
    path('createname', create_name.as_view(), name='createname'),
    path('login', login_form, name='loginform'),
    path('loggedin', logged_in, name='loggedin'),
    path('list', list_view, name='list'),
    path('classbased', class_based_view.as_view(), name='classbased'),
    path('create', create_view, name='create'),
    path('<id>/detail', detail_view, name='detail'),
    path('<id>/update', update_view, name='update'),
    path('<id>/delete', delete_view, name='delete'),
    path('classcreate', class_create_view.as_view(), name='classcreate'),
    path('<pk>/classdetail', class_detail_view.as_view(), name='classdetail'),
    path('<pk>/classupdate', class_update_view.as_view(), name='classupdate'),
    path('<pk>/classdelete', class_delete_view.as_view(), name='classdelete'),
]