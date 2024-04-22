# from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet, LogoutViewSet
from rest_framework_nested import routers
from core.product.viewsets import ProductViewSet, CategoryViewSet
router = routers.SimpleRouter()

# User
router.register(r'users', UserViewSet, basename='user')

# Authentication
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")

# Product and others
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

products_router = routers.NestedSimpleRouter(router, r'products', lookup='product')

urlpatterns = [
    *router.urls,
    *products_router.urls
]
