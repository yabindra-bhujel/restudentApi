from django.conf.urls.static import static
from mysite import settings
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import UserViewset, MyTokenObtainPairView

from menu.views import *

urlpatterns = [
    #  admin site url
    path('admin/', admin.site.urls),
    
    #  auth url
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
    #  menu url
    
    path('api/menu/', menuList),
    path('api/menu/create/', createMenu),
    path('api/menu/<int:id>/', menu_detail),
    
    
    #  blog url
    path('api/blog/', blogList),
    path('api/blog/create/', createBlog),
    path('api/blog/<int:id>/', blog_detail),
    
    #  comment url
    path('api/comment/', commentList),
    path('api/comment/create/', createComment),
    
    
    
    # table Reversed url
    
    path('api/table/', TableReversedlist),
    path('api/table/<int:id>/', userWiseTable),
    
]

router = routers.DefaultRouter()
router.register(r'users', UserViewset, basename='users')

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
