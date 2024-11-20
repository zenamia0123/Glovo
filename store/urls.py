from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'store-list', StoreListViewSet, basename='store-list')
router.register(r'store-detail', StoreDetailViewSet, basename='store-detail')
router.register(r'product-list', ProductListViewSet, basename='product-list')
router.register(r'product-detail', ProductDetailViewSet, basename='product-detail')
router.register(r'order-list', OrderListViewSet, basename='order-list')
router.register(r'order-detail', OrderDetailViewSet, basename='order-detail')
router.register(r'courier-list', CourierListViewSet, basename='courier-list')
router.register(r'courier-detail', CourierDetailViewSet, basename='courier-detail')
router.register(r'review-list', ReviewListViewSet, basename='review-list')
router.register(r'review-detail', ReviewDetailViewSet, basename='review-detail')


urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListViewSet.as_view({'get': 'list'}), name='product'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
