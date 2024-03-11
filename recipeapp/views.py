# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe, RecipeReview
from .serializers import (
    RecipeSerializer,
    RecipeDetailSerializer,
    RecipeCreateSerializer,
    RecipeUpdateSerializer,
    RecipeReviewSerializer,
    RecipeReviewCreateSerializer,
    RecipeReviewRetrieveSerializer,
)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return RecipeUpdateSerializer
        return RecipeDetailSerializer


class RecipeCreate(generics.CreateAPIView):
    serializer_class = RecipeCreateSerializer


class RecipeFilterList(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        # Add filtering logic based on URL parameters (e.g., cuisine, meal_type, ingredients)
        cuisine = self.request.query_params.get('cuisine', None)
        meal_type = self.request.query_params.get('meal_type', None)
        ingredients = self.request.query_params.getlist('ingredients', None)

        if cuisine:
            queryset = queryset.filter(cuisine__name=cuisine)
        if meal_type:
            queryset = queryset.filter(meal_type__name=meal_type)
        if ingredients:
            queryset = queryset.filter(ingredients__name__in=ingredients)

        return queryset


class RecipeReviewList(generics.ListCreateAPIView):
    queryset = RecipeReview.objects.all()
    serializer_class = RecipeReviewSerializer


class RecipeReviewDetail(generics.RetrieveAPIView):
    queryset = RecipeReview.objects.all()
    serializer_class = RecipeReviewRetrieveSerializer


class RecipeReviewCreate(generics.CreateAPIView):
    serializer_class = RecipeReviewCreateSerializer

    def create(self, request, *args, **kwargs):
        # Add logic to associate the review with a specific recipe based on request data
        # For example, you may expect a 'recipe_id' in the request data
        recipe_id = request.data.get('recipe_id', None)
        if recipe_id:
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                request.data['recipe'] = recipe.id
            except Recipe.DoesNotExist:
                return Response({"error": "Recipe not found."}, status=status.HTTP_404_NOT_FOUND)

        return super().create(request, *args, **kwargs)
