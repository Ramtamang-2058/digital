from rest_framework import routers
from backend.views import TrainerViewset ,  EventsViewset , RegistrationViewset , AttendesViewset


router = routers.DefaultRouter()


router.register(r'Trainers', TrainerViewset)
router.register(r'Registration', RegistrationViewset)
router.register(r'Attendes', AttendesViewset)
# router.register(r'Trainers', Trainer)
router.register(r'Events', EventsViewset)




urlpatterns = router.urls