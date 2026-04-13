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
            
            def validate(self, attrs):
                shop = attrs.get('shop')
                flavour = attrs.get('flavour')

                valid_flavours = shop.tea_shop.values_list('flavour', flat=True)

                if flavour not in valid_flavours:
                    raise serializers.ValidationError(
                        "The specified flavour is not available in the tea shop."
                    )

                return attrs
