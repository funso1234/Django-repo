from decimal import Decimal

from  rest_framework import serializers

from store.models import Product, Collection


# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name='collection-detail'
    )
    discount = serializers.SerializerMethodField(method_name='discount_price')

    class Meta:
        model = Product
        fields =['id', 'title', 'price', 'inventory','discount', 'collection']



    def discount_price (self, products: Product):
            return products.price * Decimal(0.10)


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['title', 'price','description', 'inventory', 'collection']




# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


