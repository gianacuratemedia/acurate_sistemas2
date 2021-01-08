from rest_framework import serializers
from .models import StripeCustomerTransfers


class Stripe_Transfer_S(serializers.ModelSerializer):

    class Meta:
        model = StripeCustomerTransfers
        fields = ['user', 'acccount_Stripe']

