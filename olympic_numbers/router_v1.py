from rest_framework import routers
from olympic.views import NocViewSet, AthleteViewSet

router = routers.DefaultRouter()
router.register(r'nocs', NocViewSet)
router.register(r'athletes', AthleteViewSet)
