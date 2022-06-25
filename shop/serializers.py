from shop.models import Pet, PetType, PetBreed, Order, Customer,Parent
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


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

    customer = serializers.SlugRelatedField(
        allow_null=True,
        slug_field='name',
        required=False,
        queryset=Customer.objects.all())

    class Meta:
        model = Order
        fields = ['id','customer', 'price', 'currency','orderdate','shop']


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

    parent = serializers.SlugRelatedField(
        allow_null=True,
        slug_field='name',
        required=False,
        queryset=Parent.objects.all())

    # customer = serializers.PrimaryKeyRelatedField(
    #     allow_null=True,
    #     required=False,
    #     queryset=Customer.objects.all())

    son = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ['id', 'name', 'birthdate', 'type', 'breed','parent', 'order','son']

    def get_son(self, pet):
        try:
            son = Pet.objects.get(parent_id=pet.id)
        except Pet.DoesNotExist:
            return 'pet not found'
        son_serializer = PetSerializer(son)
        return son_serializer.data


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.get('username')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

