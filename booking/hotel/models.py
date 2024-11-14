from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

ROOM_CHOICES = (
    ('номер свободен', 'номер свободен'),
    ('номер забранирован', 'номер забранирован')
)

ROLE_CHOICES = (
    ('simpleUser', 'simpleUser'),
    ('ownerUser', 'ownerUser')
)

TYPE_CHOICES = (
    ('люкс', 'люкс'),
    ('семейный', 'семейный'),
    ('одноместный', 'одноместный'),
    ('двухместный', 'двухместный')
)

STATUS_CHOICES = (
        ('свободен', 'свободен'),
        ('занят', 'занят'),
        ('забронирован', 'забронирован')
    )

STATUS_BOOK_CHOICES = (
    ('отменено', 'отменено'),
    ('потверждено', 'потверждено')
)


class UserProfile(AbstractUser):
    user_role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='simpleUser')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(110)], null=True, blank=True)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField()
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel_name},{self.city},{self.country}'


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=32, choices=TYPE_CHOICES)
    room_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='свободен')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField()

    def __str__(self):
        return f'{self.hotel_room} {self.room_type} {self.room_number}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_images = models.ImageField(upload_to='room_images/')


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_image')
    hotel_image = models.ImageField(upload_to='hotel_images/')


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    parent_review = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.hotel} {self.user_name} {self.stars}'


class Booking(models.Model):
    hotel_book = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_book = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room_book = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    status_book = models.CharField(max_length=32, choices=STATUS_BOOK_CHOICES)

    def __str__(self):
        return f'{self.room_book} {self.status_book} {self.hotel_book} {self.user_book}'



























