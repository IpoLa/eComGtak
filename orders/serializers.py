from rest_framework import serializers

from carts.mixins import TokenMixin

from .models import UserAddress, Order

# parse order token
# check order not complete
# nonce is coming through
# mark cart complete
# mark order done


class OrderDetailSerializer(serializers.ModelSerializer):
	# url = serializers.HyperlinkedIdentityField(view_name="order_detail_api")
	subtotal = serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = '__all__'

	def get_subtotal(self, obj):
		return obj.cart.subtotal



class OrderSerializer(serializers.ModelSerializer):
	subtotal = serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = '__all__'

	def get_subtotal(self, obj):
		return obj.cart.subtotal


class OrderCreateSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='document_detail_api')
    class Meta:
        model = Order
        fields = '__all__'
    def create(self, validated_data):
        # Product.objects.get(title=title)
        order = Order.objects.create(**validated_data)
        return order

    def update(self, instance, validated_data):
        instance.save()
        return instance


class UserAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserAddress
		fields = [
			"id",
			"user",
			"type",
			"street",
			"city",
			"zipcode",
		]