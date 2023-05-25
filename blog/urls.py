from django.urls import path
from .views import post_detail, post_share,post_comment,user_register,user_login,dashboard,delete,post_list
# from .views import PostListView

app_name = 'blog'

urlpatterns = [
    path('',post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/',post_comment , name='post_comment'),
    path('post/register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('profile/', dashboard, name='profile'),
    path('post/<int:pk>/delete', delete, name='delete'),

]
