from django.contrib import admin
from review.models import Ticket, Review


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'user', 'ticket', 'rating')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)