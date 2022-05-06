from rest_framework import serializers
from .models import Client, Driver
from rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'address': self.validated_data.get('address', ''),
            'location': self.validated_data.get('location', ''),
        }


class ClientDetailSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    class Meta:
        model = Client
        fields = ('username', 'email', 'phone', 'location')

        read_only_fields = ('username', 'email')

class ClientSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    # variation_set = VariationSerializer(many=True)
    # product_image = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    class Meta:
        model = Client
        fields = '__all__'
    def create(self, validated_data):
        username = validated_data["username"]
        # Product.objects.get(title=title)
        client = Client.objects.create(**validated_data)
        return client

    def update(self, instance, validated_data):
        instance.username = validated_data["username"]
        instance.save()
        return instance






# Driver Serializers

class DriverRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'address': self.validated_data.get('address', ''),
            'location': self.validated_data.get('location', ''),
        }


class DriverDetailSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    class Meta:
        model = Driver
        fields = ('username', 'email', 'phone', 'location')

        read_only_fields = ('username', 'email')

class DriverSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    # variation_set = VariationSerializer(many=True)
    # product_image = serializers.SerializerMethodField()
    class Meta:
        model = Driver
        fields = '__all__'


class DriverDetailUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='clients_detail_api')
    class Meta:
        model = Driver
        fields = '__all__'
    def create(self, validated_data):
        username = validated_data["username"]
        # Product.objects.get(title=title)
        driver = Driver.objects.create(**validated_data)
        return driver

    def update(self, instance, validated_data):
        instance.username = validated_data["username"]
        instance.save()
        return instance