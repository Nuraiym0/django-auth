from rest_framework import serializers

from .models import User
# cd/Desktop/python23/lections

class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)


    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')


    def validate(self, attrs):
        # attrs = {'email':'some@gmail.com', 'password':'1234', 'password_confirm':'1234'}
        pass1 = attrs.get('password')
        pass2 =attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('passwords do not match')
        return attrs


    def validate_email(self, email):
        # email = 'some@gmail.com'
        if User.objects.filter(email=email). exists():
            raise serializers.ValidationError('user with this email alredy exists')
        return email 
    

    def create(self, validated_data):
        # validated_data = {'email':'some@gmail.com', 'password':'1234', 'password_confirm':'1234'}
        return User.objects.create_user(**validated_data)
















