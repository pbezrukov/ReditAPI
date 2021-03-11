from django.urls import path
from .views import PostsView, OnePostView


urlpatterns = [
    path("", PostsView.as_view()),
    path("<int:pk>", OnePostView.as_view())

]
