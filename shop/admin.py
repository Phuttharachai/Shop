from django.contrib import admin
from shop.models import PetType, Pet, PetBreed, Order, Customer,Dad,Mom,Child


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
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):
    pass

@admin.register(Dad)
class Dad(admin.ModelAdmin):
    pass

@admin.register(Mom)
class Mom(admin.ModelAdmin):
    pass

@admin.register(Child)
class Child(admin.ModelAdmin):
    pass


