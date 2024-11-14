from django.urls import path, include
from .views import *
from rest_framework import routers


routers = routers.DefaultRouter()

routers.register(r'hotel/', HotelListViewSet, basename='hotel_list'),
routers.register(r'hotel_detail/', HotelDetailViewSet, basename='hotel_detail'),
routers.register(r'user/', UserProfileListViewSet, basename='user_list'),
routers.register(r'user_detail/', UserProfileDetailViewSet, basename='user_detail'),
routers.register(r'room/', RoomListViewSet, basename='room_list'),
routers.register(r'room_detail', RoomDetailViewSet, basename='room_detail'),
routers.register(r'room_photos', RoomImageViewSet, basename='roomphoto_list'),
routers.register(r'hotel_photos', HotelImageViewSet, basename='hotelphotos_list'),
routers.register(r'review', ReviewViewSet, basename='review_list'),
routers.register(r'booking', BookingViewSet, basename='booking_list')

urlpatterns = [
    path('', include(routers.urls))
]
