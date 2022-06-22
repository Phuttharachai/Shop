from rest_framework import permissions, viewsets,mixins
from shop.models import Pet, Order ,Customer
from shop.serializers import PetSerializer, OrderSerializer ,CustomerSerializer

class PetViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
    A ViewSet for Pets CRUD API.
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        pet = Pet.objects.get(pk=kwargs['pk'])
        serializer = AccountRoomSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """
    A ViewSet for creating pets orders API.
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
        serializer = AccountRoomSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):

    """
    A ViewSet for creating pets Customer API.
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
        serializer = AccountRoomSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

