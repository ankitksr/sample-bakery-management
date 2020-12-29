from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bakery.inventory.models import BakeryItem, Ingredient, Order
from bakery.inventory.serializers import IngredientSerializer, BakeryItemSerializer, OrderSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """A viewset for Ingredient objects"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAdminUser]


class BakeryItemViewSet(viewsets.ModelViewSet):
    """A viewset for BakeryItem objects"""
    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class OrderViewSet(viewsets.ModelViewSet):
    """A viewset for Order objects"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
