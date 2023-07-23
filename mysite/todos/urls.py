from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("v1/", views.get_routes),
    path("v1/todos/", views.TodoMixinList.as_view()),
    path("v1/todos/create/", views.TodoMixinCreate.as_view()),
    path("v1/todos/<int:pk>/", views.TodoMixinRetrieve.as_view(), name="product-detail"),
    path("v1/todos/<int:pk>/update/", views.TodoMixinUpdate.as_view()),
    path("v1/todos/<int:pk>/delete/", views.TodoMixinDestroy.as_view()),
]
