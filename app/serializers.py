from rest_framework import serializers
from .models import BootcampRegistration

class BootcampRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootcampRegistration
        fields = ['full_name','email', 'role']
        read_only_fields = ['registered_at']
    
    def validate_email(self, value):
        #  = self.initial_data.get('bootcamp_name')
        if BootcampRegistration.objects.filter(email=value,).exists():
            raise serializers.ValidationError("This email is already registered for the selected bootcamp.")
        return value