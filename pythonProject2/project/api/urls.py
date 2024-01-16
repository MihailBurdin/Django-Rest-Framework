from django.urls import path
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'posts', PostsView)
# urlpatterns = router.urls
urlpatterns = [
    path('', PostsView.as_view({'get': 'list', 'post': 'create'})),
    path('posts/', postsList),
    path('posts/<int:pk>/', postGet),
    path('postsdel/<int:pk>/', postDel),
    path('postsAdd/', postCreate),
    path('postsPatch/<int:pk>/', postPatch),
    path('postsPut/<int:pk>/', postPut),
]