from shop.models import Pet, PetType, PetBreed, Order, Customer,Dad
from rest_framework import serializers, validators

#from dad.serializers import DadSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'address']

class OrderSerializer(serializers.ModelSerializer):

    def validate_shop(self, value):
        """
        Raises validation error if any of the pet ids provided was sold before.
        """
        shop_ids = [shop.id for shop in value]
        sold_shop = Pet.objects.filter(pk__in=shop_ids, order__isnull=False)
        if sold_shop:
            raise serializers.ValidationError(
                'one or more of the provided pets were already sold.')
        return value

    class Meta:
        model = Order
        fields = ['id', 'price', 'currency','orderdate','shop']


class PetSerializer(serializers.ModelSerializer):
    # to send pet type name instead of id in the requests
    type = serializers.SlugRelatedField(
        slug_field='name',
        error_messages={
            'does_not_exist': 'Pet type does not exist.',
        },
        queryset=PetType.objects.all())

    # to send pet breed name instead of id in the requests
    breed = serializers.SlugRelatedField(
        slug_field='name',
        error_messages={
            'does_not_exist': 'Pet breed does not exist.',
        },
        queryset=PetBreed.objects.all())

    order = serializers.PrimaryKeyRelatedField(
        allow_null=True,
        required=False,
        queryset=Order.objects.all())

    class Meta:
        model = Pet
        fields = ['id', 'name', 'birthdate', 'type', 'breed', 'order']

class PetDadSerializer(serializers.ModelSerializer):
    dad = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = (
            'id',
            'name',
            'birthdate',
            'type',
            'breed',
            'order',
            'dad',
        )

    def get_dad(self, shop):
        dad = Dad.objects.get(pet_id=shop.id)
        dad_serializer = DadSerializer(dad)
        return dad_serializer.data



