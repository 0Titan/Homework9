from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
from django.utils.safestring import mark_safe




class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date', 'get_image']
    list_filter = ['auction', 'created_dt']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    def get_image(selfself, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="90"')

    get_image.short_description = 'Изображение'

    @admin.action(description='Отменить возможность торга')
    def make_auction_as_false(selfself, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(selfself, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        (
            'Общее',
            {'fields': ('title', 'description', 'image')}
        ),
        (
            'Финансы',
            {'fields': ('price', 'auction'), 'classes': ['collapse']}
        )
    )


admin.site.register(Advertisement, AdvertisementAdmin)
