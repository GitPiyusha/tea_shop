from rest_framework import serializers

from .models import CustomerFeedbackModel

class FeedbackSerializer(serializers.ModelSerializer):
            rating = serializers.FloatField(min_value=0, max_value=5)
            feedback = serializers.CharField(required=False, allow_blank=True)

            class Meta:
                model = CustomerFeedbackModel
                fields = '__all__'

            def validate(self, data):
                if data['rating'] < 4:
                    if not data.get('feedback'):
                        raise serializers.ValidationError("Feedback is required for ratings below 4.")
                    return data
                return data
