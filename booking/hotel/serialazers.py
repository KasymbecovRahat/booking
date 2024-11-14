from rest_framework import serializers
from .models import *


class UserProfileListSerialazer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'age', 'user_role']


class UserProfileDetailSerialazer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class RoomImageSerialazer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'


class ReviewSerialazer(serializers.ModelSerializer):
    user_name = UserProfileListSerialazer()

    class Meta:
        model = Review
        fields = ['id', 'user_name', 'text', 'parent_review']


class HotelImageSerialazer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomListSerialazer(serializers.ModelSerializer):
    room_images = RoomImageSerialazer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'price', 'all_inclusive',
                  'room_images']


class RoomDetailSerialazer(serializers.ModelSerializer):
    room_images = RoomImageSerialazer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'price', 'all_inclusive',
                  'room_description', 'room_images']


class HotelListSerialazer(serializers.ModelSerializer):
    hotel = HotelImageSerialazer(read_only=True, many=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    reviews = ReviewSerialazer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'stars', 'hotel_video', 'created_date',  'hotel', 'reviews']


class HotelDetailSerialazer(serializers.ModelSerializer):
    hotel_image = HotelImageSerialazer(many=True, read_only=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    owner = UserProfileListSerialazer()
    reviews = ReviewSerialazer(read_only=True, many=True)
    rooms = RoomDetailSerialazer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = [
            'hotel_name', 'country', 'city', 'stars', 'hotel_video', 'created_date', 'hotel_image', 'owner',
            'hotel_description', 'reviews', 'rooms'
        ]


class BookingSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'