from django.contrib import admin
from .models import Questions, Choice
# Register your models here.

# change site header
admin.site.site_header = "Voting System"

admin.site.site_title = "Voting System Area"
admin.site.index_title = "Voting Admin Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': [
                  'pub_date'], 'classes':['collapse']}),
                 ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionAdmin)
# admin.site.register(Questions)
