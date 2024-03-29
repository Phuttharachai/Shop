from rest_framework import permissions, viewsets,mixins, status,serializers
from shop.models import Pet, Order ,Customer
from shop.serializers import PetSerializer, OrderSerializer ,CustomerSerializer
from rest_framework.response import Response


class PetViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
    A ViewSet for Pets CR API.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **pet):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request, *args, **kwarg):
        print(args)
        print(kwarg)
        pet = Pet.objects.filter(order__customer_id=kwarg['pk'])
        serializer = PetSerializer(pet, many=True)
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

