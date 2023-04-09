
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import UserViewset, MyTokenObtainPairView

from menu.views import menuList, createMenu, menu_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/menu/', menuList),
    path('api/menu/create/', createMenu),
    path('api/menu/<int:id>/', menu_detail),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewset, basename='users')

urlpatterns += router.urls
