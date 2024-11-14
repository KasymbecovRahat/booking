from rest_framework.permissions import BasePermission
from .views import permissions


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCrud(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'


class CheckPost(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'свободен':
            return True
        return False


class CheckBooking(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'simpleUser':
            return True
        return False


class CheckReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user


class CheckUpdateRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.hotel_room.owner


class CheckUserBooking(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_book


class CheckImage(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


class CheckUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.user_role == permissions.IsAuthenticated:
            return False
        return True
