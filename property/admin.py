from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building',
                    'construction_year', 'town',
                    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)
    inlines = [
        FlatsInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'pure_phone']
    raw_id_fields = ('flats',)
    inlines = [
        FlatsInline,
    ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
