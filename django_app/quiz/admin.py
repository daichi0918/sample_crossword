from django.contrib import admin
from .models import Quiz,VerticalKeyword,HorizonalKeyword
# Register your models here.

admin.site.register(Quiz)
admin.site.register(VerticalKeyword)
admin.site.register(HorizonalKeyword)