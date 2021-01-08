from django.urls import path
from django.conf.urls import url
from Premium_k import views
from .views import save_stripe_info_pa, TransferStripe, Stripe_Transfer_User

urlpatterns = [
 path('test-payment/', views.test_payment),
 path('payment-method/', views.payment_method),
 path('save-stripe-info/plan-anual/', save_stripe_info_pa.as_view(), name="plan_anual"), 
 path('save-stripe-info/plan-mensual/', views.save_stripe_info_pm),
 path('confirm-payment-intent/', views.confirm_payment_intent),
 path('cancel_subscription_p/', views.CancelSub_FP), 
 path('consultar_saldo/', views.ConsultSaldo),

 #Realizar consulta del id de la cuenta del tutor en Stripe 
 path('datos-cuenta-user/<int:user>', Stripe_Transfer_User.as_view(), name="cuenta_stripe_user"), 

 #Realizar transferencia 
 path('transferencias/', TransferStripe.as_view(), name="transferencias"), 
]
