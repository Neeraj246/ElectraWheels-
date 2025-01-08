from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Logintable)
admin.site.register(UserTable)
admin.site.register(StationTable)
admin.site.register(ServiceTable)
admin.site.register(FeedbackTable)
admin.site.register(ComplaintTable)
admin.site.register(SpareTable)
admin.site.register(SlotTable)
admin.site.register(SpareBookingTable)
admin.site.register(Alert)
admin.site.register(Review)