from django.contrib import admin
from .models import DogInfo,DogBreedInfo,CatInfo,CatBreedInfo,RabbitBreedInfo,RabbitInfo

# Register your models here.
admin.site.register(DogInfo)
admin.site.register(DogBreedInfo)
admin.site.register(CatInfo)
admin.site.register(CatBreedInfo)
admin.site.register(RabbitInfo)
admin.site.register(RabbitBreedInfo)
