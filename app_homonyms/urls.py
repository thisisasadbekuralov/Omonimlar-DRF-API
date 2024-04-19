from rest_framework import routers

from .views import HomonymsViewSet, HomonymsListView

router = routers.DefaultRouter()
router.register(r'detail', HomonymsViewSet, basename='homonyms_detail')
router.register(r'', HomonymsListView, basename='homonyms')

urlpatterns = router.urls


# urlpatterns = [
#     path('', HomonymsViewSet.as_view(), name='homonyms'),
# ]