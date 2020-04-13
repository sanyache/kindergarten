from django.contrib import admin
from django import forms
from .models import *
# Register your models here.


class TutorInLine(admin.TabularInline):
    """
    class for rendering m2m relations
    """
    model = Group.tutor.through


class SectionInLine(admin.TabularInline):
    """
    class for rendering m2m relations
    """
    model = Group.section.through


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):

    model = Tutor
    list_display = ('last_name', 'first_name', 'tutor_position', 'birthday', 'get_group',
                    'get_section')
    list_filter = ['tutor_position']

    def get_group(self, obj):
        return obj.group_tutor.all()

    def get_section(self, obj):
        return obj.section_tutor.all()


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

    model = Section


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    #model = Group
    exclude = ('tutor', 'section')
    inlines = (TutorInLine, SectionInLine)
    list_display = ('name', 'age_group')
