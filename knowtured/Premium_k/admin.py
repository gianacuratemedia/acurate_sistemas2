from django.contrib import admin
from .models import StripeCustomer, StripeCustomerTransfers

# Register your models here.

admin.site.register(StripeCustomer)
admin.site.register(StripeCustomerTransfers)
