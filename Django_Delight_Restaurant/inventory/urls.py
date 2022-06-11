from django import views
from django.urls import path
from . import views


urlpattern=[
    path("", views.index, name="index"),
    path("/ingredients/", views.ingredients, name="ingredient"),
    path("/menu-item", views.menuItem, name="menuitem"),
    path("/purchases", views.purchases, name="purchases"),
    path("/profit-and-revenue", views.profitRevenue, name="profit_and_revenue"),
    path("/ingredients/add", views.CreateIngredientView.as_view(), name="add_ingredient"),
    path("/ingredients/delete", views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path("/ingredients/<slug:pk>/update", views.UpdateIngredientView.as_view(), name="update_ingredient"),
    
]
