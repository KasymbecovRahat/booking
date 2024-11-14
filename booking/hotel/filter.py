from .models import *
from django_filters import FilterSet


class HotelFilterSet(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
            'country': ['exact'],
            'city': ['exact'],
        }


class RoomFilterSet(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_number': ['exact'],
            'price': ['gt', 'lt'],
        }