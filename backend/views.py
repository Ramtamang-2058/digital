from backend.serializers import Attendesserializer, Eventsserializer, Registrationserializer, Trainerserializer
from rest_framework import generics , viewsets 
from backend.models import Trainer , Registration , Attendes , Events

class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = Trainerserializer


class RegistrationViewset(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = Registrationserializer


class AttendesViewset(viewsets.ModelViewSet):
    queryset = Attendes.objects.all()
    serializer_class = Attendesserializer


class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = Eventsserializer