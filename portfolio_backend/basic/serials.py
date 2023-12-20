from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.serializers import ValidationError
from .models import * 


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


    def validate(self , data):
        if data['end_date']:
            if data['start_date'] > data['end_date']:
                raise ValidationError('Start Date cannot be greater than End Date')
        return data 


