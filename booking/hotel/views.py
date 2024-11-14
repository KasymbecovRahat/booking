from rest_framework import viewsets, permissions
from .models import *
from .serialazers import *
from .filter import HotelFilterSet, RoomFilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .perrmision import *


class UserProfileListViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerialazer


class UserProfileDetailViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerialazer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerialazer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilterSet
    search_fields = ['hotel_name', 'city', 'country']
    permission_classes = [CheckCrud, CheckUser, permissions.IsAuthenticated]


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerialazer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilterSet
    search_fields = ['hotel_name', 'city', 'country']
    permission_classes = [CheckCrud, CheckPost, CheckUser, permissions.IsAuthenticated]


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerialazer
    permission_classes = [CheckImage]


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerialazer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['room_number']
    ordering_fields = ['price']
    filterset_class = RoomFilterSet
    permission_classes = [CheckUpdateRoom, CheckRoom]


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerialazer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['room_number']
    ordering_fields = ['price']
    filterset_class = RoomFilterSet
    permission_classes = [CheckRoom, CheckUpdateRoom]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialazer
    permission_classes = [permissions.IsAuthenticated, CheckOwner, CheckReview ]


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerialazer
    permission_classes = [CheckImage]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialazer
    permission_classes = [CheckBooking, CheckUserBooking]

