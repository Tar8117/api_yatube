from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename="Post")
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename="Comment")


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
