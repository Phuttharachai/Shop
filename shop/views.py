from rest_framework import permissions, viewsets, mixins
from shop.models import Pet, Order ,Customer
from shop.serializers import PetSerializer, OrderSerializer ,CustomerSerializer

class PetViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for Pets CRUD API.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.AllowAny]


class OrderViewSet(viewsets.ModelViewSet, viewsets.GenericViewSet):
    """
    A ViewSet for creating pets orders API.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

class CustomerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet for creating pets Customer API.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]