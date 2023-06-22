from django.urls import path
from .views import post_detail, post_share,post_comment_add,user_register,user_login,profile,post_delete,user_logout,post_add,post_update
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail, name='post_detail'),
    path('<int:post_id>/share/',post_share, name='post_share'),
    path('<int:post_id>/comment/',post_comment_add, name='post_comment'),
    path('post/register/',user_register, name='user_register'),
    path('login/',user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('post-add/', post_add, name='post_add'),
    path('post/<int:post_id>/update', post_update, name='post_update'),

    path('profile/',profile, name='profile'),
    path('post/<int:pk>/delete',post_delete, name='post_delete'),
]
