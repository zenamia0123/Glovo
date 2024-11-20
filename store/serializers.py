from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role', 'email', 'password']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role', 'email', 'password']


class StoreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'description']


class StoreDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'description', 'contact_info', 'address', 'owner']


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description']


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'quantity', 'store']


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ['image']


class OrderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client', 'products']


class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client', 'products', 'status_order', 'delivery_address', 'courier', 'created_at']


class CourierListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['user', 'status']


class CourierDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['user', 'status', 'current_order']


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['client', 'store', 'courier']


class ReviewDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
