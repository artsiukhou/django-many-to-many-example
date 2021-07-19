from django.urls import include, path
from rest_framework import routers

from backend.views import RecipeViewSet, IngredientViewSet

router = routers.DefaultRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'ingredient', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]