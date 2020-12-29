from rest_framework import serializers

from bakery.inventory.models import Ingredient, BakeryItem, BakeryItemIngredient, Order


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class BakeryItemIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='ingredient.name')
    class Meta:
        model = BakeryItemIngredient
        fields = ('ingredient', 'quantity_percentage',)


class BakeryItemSerializer(serializers.ModelSerializer):
    ingredients = BakeryItemIngredientSerializer(source='bakeryitemingredient_set', many=True)

    def create(self, validated_data):
        ingredients = validated_data.pop('bakeryitemingredient_set', [])
        instance = BakeryItem.objects.create(**validated_data)
        for ingredient_data in ingredients:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_data['ingredient']['name'])
            instance.ingredients.add(
                ingredient,
                through_defaults={'quantity_percentage': ingredient_data['quantity_percentage']}
            )
        return instance
    
    def update(self, instance, validated_data):
        ingredients = validated_data.pop('bakeryitemingredient_set', [])
        print(ingredients)
        for ingredient_data in ingredients:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_data['ingredient']['name'])
            instance.ingredients.add(
                ingredient,
                through_defaults={'quantity_percentage': ingredient_data['quantity_percentage']}
            )
        return instance

    class Meta:
        model = BakeryItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
