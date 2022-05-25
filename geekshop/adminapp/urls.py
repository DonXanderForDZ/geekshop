from django.urls import path
import adminapp.views as adminapp

app_name = "admin"

urlpatterns = [
    path("users/", adminapp.users, name="users"),
    path("users/create/", adminapp.create_user, name="create_user"),
    path("users/update/<int:pk>/", adminapp.update_user, name="update_user"),
    path("users/delete/<int:pk>/", adminapp.delete_user, name="delete_user"),

    path("categories/", adminapp.categories, name="categories"),
    path("category/create/", adminapp.create_category, name="create_category"),
    path("category/update/<int:pk>/", adminapp.update_category, name="update_category"),
    path("category/delete/<int:pk>/", adminapp.delete_category, name="delete_category"),

    path("products/<int:pk>/", adminapp.products, name="products"),
    path("product/<int:pk>/create/", adminapp.create_product, name="create_product"),
    path("product/update/<int:pk>/", adminapp.update_product, name="update_product"),
    path("product/delete/<int:pk>/", adminapp.delete_product, name="delete_product"),
]

