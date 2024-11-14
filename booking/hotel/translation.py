from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'city', 'country')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room_description',)
