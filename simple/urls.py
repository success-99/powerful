from django.urls import path
from .views import list_view,delete,update,create,post_detail
app_name='simple'
urlpatterns = [
    path('post/<int:pk>/delete', delete, name='delete'),
    path('post/<int:pk>/update', update, name='update'),
    path('post/new/', create, name='create'),
    path('', list_view, name='index'),
    path('post/<int:pk>/',post_detail, name='detail'),
]