from django.conf import settings
from django.shortcuts import reverse
from Usuarios_k.models import User

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    active=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class StripeCustomerTransfers(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    acccount_Stripe = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
