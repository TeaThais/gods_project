from django.contrib import admin, messages
from .models import Goddesses, Category


class ConsortFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('has consort', 'has consort'),
            ('single', 'single')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'has consort':
            return queryset.filter(consort__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(consort__isnull=True)


@admin.register(Goddesses)
class GoddessesAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief_info', 'is_published', 'cat')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    list_display_links = ('title',)
    ordering = ('title',)
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_draft')
    search_fields = ('title', 'cat__name')
    list_filter = (ConsortFilter, 'cat__name', 'is_published')

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