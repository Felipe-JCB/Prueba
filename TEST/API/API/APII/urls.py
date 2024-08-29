from rest_framework.routers import DefaultRouter
from API.APII.views import Jsonviewset

router = DefaultRouter()
router.register('Json', Jsonviewset, basename='json')
urlpatterns = router.urls