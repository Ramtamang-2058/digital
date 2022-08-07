from backend.models import Attendes, Events, Registration, Trainer
from rest_framework import serializers

class Trainerserializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class Registrationserializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class Attendesserializer(serializers.ModelSerializer):
    class Meta:
        model = Attendes
        fields = '__all__'


class Eventsserializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'