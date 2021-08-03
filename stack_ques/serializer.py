from rest_framework import serializers
from .models import Questions


class QuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('__all__')


