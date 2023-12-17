from rest_framework.routers import SimpleRouter
from catalog.views.admin import CategoryViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet, basename='Category_Admin')
urlpatterns = [] + router.urls
