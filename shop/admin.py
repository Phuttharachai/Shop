from django.contrib import admin
from shop.models import PetType, Pet, PetBreed, Order, Customer


@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PetBreed)
class PetBreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CumtomerAdmin(admin.ModelAdmin):
    pass