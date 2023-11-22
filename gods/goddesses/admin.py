from django.contrib import admin, messages
from .models import Goddesses, Category

# Register your models here.


@admin.register(Goddesses)
class GoddessesAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief_info', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ('title',)
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_draft')

    def brief_info(self, gods: Goddesses):
        return f"Description {len(gods.content)} symbols."

    def set_published(self, request, queryset):
        count = queryset.update(is_published=Goddesses.Status.PUBLISHED)
        self.message_user(request, f"{count} items were changed.")

    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Goddesses.Status.DRAFT)
        self.message_user(request, f"{count} items were changed.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name',)
    ordering = ('name',)

# admin.site.register(Goddesses, GoddessesAdmin)