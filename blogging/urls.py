from django.urls import path
from rest_framework import routers
from blogging.views import list_view, detail_view
from blogging.views import PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
