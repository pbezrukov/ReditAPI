from django.urls import path
from .views import PostListCreateView, PostDetailView


urlpatterns = [
    path("", PostListCreateView.as_view(), name='post'),
    path("<int:pk>", PostDetailView.as_view(), name='get_delete_update_post')

]
