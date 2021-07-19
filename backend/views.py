from django.http.response import HttpResponse
from rest_framework import viewsets, serializers

from backend.models import Recipe, Ingredient, IngredientInRecipe


class GetIngredientInRecipeSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source="ingredient.id", read_only=True)
    name = serializers.PrimaryKeyRelatedField(source="ingredient.name", read_only=True)

    class Meta:
        model = IngredientInRecipe
        fields = ("id", "name", "amount")


class GetRecipeSerializer(serializers.ModelSerializer):
    ingredients = GetIngredientInRecipeSerializer(source="ingredientinrecipe_set", many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ("ingredients", "name", "id")


class CreateIngredientInRecipeSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(required=True, queryset=Ingredient.objects.all())
    amount = serializers.IntegerField(required=True)

    class Meta:
        #model = IngredientInRecipe
        fields = ("id", "amount")

class CreateRecipeSerializer(serializers.ModelSerializer):
    ingredients = CreateIngredientInRecipeSerializer(source="ingredientinrecipe_set", many=True)

    class Meta:
        model = Recipe
        fields = ("ingredients", "name", "id")

    def create(self, validated_data):
        rec = Recipe.objects.create(name=validated_data["name"])
        for ing in validated_data["ingredientinrecipe_set"]:
            ingredient = ing["id"]
            amount = ing["amount"]
            rec.ingredients.add(ingredient, through_defaults={"amount": amount})
        return rec


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = GetRecipeSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreateRecipeSerializer
        return super().get_serializer_class()


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("__all__")


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
