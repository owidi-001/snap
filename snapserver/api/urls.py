from myapp.views import UserViewSet,PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'post',PostViewSet,basename='post')

urlpatterns = router.urls