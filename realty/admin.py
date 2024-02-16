from django.contrib import admin
from realty.models import Rooms, TypeRealty, TypeTransaction, Realty, RealtyPhoto


@admin.register(TypeRealty)
class TypeRealtyAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            else:
                if obj.user != request.user:
                    return False
                else:
                    return True


@admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(TypeTransaction)
class TypeTransaction(admin.ModelAdmin):
    list_display = ('transaction',)


@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'room', 'price', 'title')


@admin.register(RealtyPhoto)
class RealtyPhoto(admin.ModelAdmin):
    list_display = ('realty', 'photo')
