from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet, basename='Post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
