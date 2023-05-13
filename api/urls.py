from django.urls import path
from .views import PostList

app_name = "api"


urlpatterns = [
        path("post/",PostList.as_view()),
]
