from rest_framework import permissions, viewsets,mixins, status,serializers
from shop.models import Pet, Order ,Customer
from shop.serializers import PetSerializer, OrderSerializer ,CustomerSerializer
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from rest_framework import exceptions

class PetViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
    A ViewSet for Pets CR API.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def retrieve(self, request, *args, **kwargs):
    #     pet = Pet.objects.get(pk=kwargs['pk'])
    #     serializer = PetSerializer(pet)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request, format=None):
    #     authentication_classes = [SessionAuthentication, BasicAuthentication]
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)

    # def retrieve(self,requst, *args, **kwargs):
    #     a = Customer.name
    #     b = Order.objects.get('customer')
    #     if a==b:
    #       pet = Pet.objects.get(pk=kwargs['pk'])
    #       serializer = PetSerializer(pet)
    #       return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         raise 'You are not the owner'

    def retrieve(self,requst, *args, **kwargs):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        order = Pet.order
        customer = Customer.name
        if order and customer:
            owner = authenticate(order=order, customer=customer)
            if owner:
                pet = Pet.objects.get(pk=kwargs['pk'])
                serializer = PetSerializer(pet)
                raise Response(serializer.data, status=status.HTTP_200_OK)
        else:
            msg = 'You are not the owner'
            raise serializers.ValidationError(msg, code='authorization')
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
    A ViewSet for CR pets orders API.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):

    """
    A ViewSet for CR Customer API.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

