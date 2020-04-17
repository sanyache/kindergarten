from django.contrib import admin
from .models import PersonInLine
# Register your models here.


@admin.register(PersonInLine)
class PersonInLine(admin.ModelAdmin):

    model = PersonInLine
    list_display = ('child_last_name','wish_year','group_age', 'privilege', 'created', 'is_approve')
