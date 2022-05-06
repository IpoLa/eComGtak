from rest_framework import serializers


from orders.models import UserAddress, UserCheckout
from products.models import Variation


from .models import CartItem, Cart
from .mixins import TokenMixin

"""
{
"cart_token": "12345", 
"billing_address": 1,
"shipping_address": 1,
"checkout_token": "12345",
}
"""

class CartDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'



class CartCreateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='document_detail_api')
    class Meta:
        model = Cart
        fields = '__all__'
    def create(self, validated_data):
        # Product.objects.get(title=title)
        cart = Cart.objects.create(**validated_data)
        return cart

    def update(self, instance, validated_data):
        instance.save()
        return instance




# CartItem Serializers
class CartItemDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = CartItem
		fields = '__all__'



class CartItemCreateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='document_detail_api')
    class Meta:
        model = CartItem
        fields = '__all__'
    def create(self, validated_data):
        # Product.objects.get(title=title)
        cartItem = CartItem.objects.create(**validated_data)
        return cartItem

    def update(self, instance, validated_data):
        instance.save()
        return instance
