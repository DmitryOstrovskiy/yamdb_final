from django.urls import include, path
from rest_framework import routers

from .views import (ApiSignup, CategoryViewSet, CommentViewSet, GenreViewSet,
                    GetApiToken, ReviewViewSet, TitleViewSet, UsersViewSet)

router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categorys')
router.register('genres', GenreViewSet, basename='genres')
router.register('users', UsersViewSet, basename='user')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register((
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments'),
    CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/auth/', include([
        path('token/', GetApiToken.as_view(), name='get_token'),
        path('signup/', ApiSignup.as_view(), name='signup')
    ])),
    path('v1/', include(router.urls)),
]
