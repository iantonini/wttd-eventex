from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptioModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'created_at')
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'Inscrito hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptioModelAdmin)
