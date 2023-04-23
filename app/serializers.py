from rest_framework.serializers import ModelSerializer
from .models import *

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ['name']