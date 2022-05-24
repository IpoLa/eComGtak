from rest_framework import serializers


from .models import Category, Product, Variation, HomeCategory, Slide


# class VariationSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Variation
# 		fields = [
# 			"id",
# 			"title",
# 			"price",
# 		]



class ProductDetailUpdateSerializer(serializers.ModelSerializer):
	# variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			# "variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None

	def create(self, validated_data):
		title = validated_data["title"]
		Product.objects.get(title=title)
		product = Product.objects.create(**validated_data)
		return product

	def update(self, instance, validated_data):
		instance.title = validated_data["title"]
		instance.save()
		return instance
	# def update


class ProductDetailSerializer(serializers.ModelSerializer):
	# variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			# "variation_set",
		]

	def get_image(self, obj):
		return obj.productimage_set.first().image.url




class ProductSerializer(serializers.ModelSerializer):
	# url = serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	# variation_set = VariationSerializer(many=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = "__all__"

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None



class CategorySerializer(serializers.ModelSerializer):
	# url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	product_set = ProductSerializer(many=True)
	class Meta:
		model = Category
		fields = [
			# "url",
			"id",
			"title",
			"description",
			"product_set", ## obj.product_set.all()
			'CategoryImage',
			#"default_category",
		]


class ProdByCatSerializer(serializers.ModelSerializer):
    	# url = serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	# variation_set = VariationSerializer(many=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = ["id", "title", "image", "description", "price"]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None


class CategoryByProductSerializer(serializers.ModelSerializer):
    	# url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	product_set = ProdByCatSerializer(many=True)
	class Meta:
		model = Category
		fields = [
			"product_set", ## obj.product_set.all()
		]


class HomeCategorySerializer(serializers.ModelSerializer):
    	# url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	# product_home_set = ProductSerializer(many=True)
	class Meta:
		model = HomeCategory
		fields = [
			# "url",
			"id",
			"title",
			"description",
			# "product_home_set", ## obj.product_set.all()
			'homeCategoryImage'
			#"default_category",
		]



class SlideSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slide
		fields = "__all__"
	