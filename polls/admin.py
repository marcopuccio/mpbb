from django.contrib import admin

from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    """
    Create a inline representation to be used in QuestionAdmin.
    """
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Question Admin Customization
    """
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently'
        )
    fieldsets = [
        (None, {
            'fields': ['question_text']
            }
        ),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
            }
        )]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']