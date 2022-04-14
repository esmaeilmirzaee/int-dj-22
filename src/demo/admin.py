from django.contrib import admin

from .models import Post


# a new customized method
def toggle_valid(modeladmin, request, queryset):
    if modeladmin.valid:
        queryset.update(valid=False)
    else:
        queryset.update(valid=True)


toggle_valid.short_description = 'toggle valid'


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'valid')
    list_filter = ['valid']
    search_fields = ['title']
    list_display = ['title', 'valid', 'combine_title_and_valid']

    def combine_title_and_valid(self, obj):
        return f"{obj.title.upper()} - {str(obj.valid).lower()}"


admin.site.register(Post, PostAdmin)
