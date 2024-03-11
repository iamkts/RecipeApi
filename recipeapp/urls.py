# urls.py

from django.urls import path
from .views import (
    RecipeList,
    RecipeDetail,
    RecipeCreate,
    RecipeFilterList,
    RecipeReviewList,
    RecipeReviewDetail,
    RecipeReviewCreate,
)

urlpatterns = [
    # Recipe operations
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/create/', RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/filter/', RecipeFilterList.as_view(), name='recipe-filter'),

    # Recipe review operations
    path('reviews/', RecipeReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', RecipeReviewDetail.as_view(), name='review-detail'),
    path('reviews/create/', RecipeReviewCreate.as_view(), name='review-create'),
]
