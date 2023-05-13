from django.urls import path
from .views import PostList,PostDetail

app_name = "api"


urlpatterns = [
        path("post/",PostList.as_view()),
        path("post/<int:pk>/", PostDetail.as_view()),

]
