from django.urls import path
from django.conf.urls import url
from Premium_k import views
from .views import save_stripe_info_pa

urlpatterns = [
 path('test-payment/', views.test_payment),
 path('payment-method/', views.payment_method),
 path('save-stripe-info/plan-anual/', save_stripe_info_pa.as_view(), name="plan_anual"), 
 path('save-stripe-info/plan-mensual/', views.save_stripe_info_pm),
 path('confirm-payment-intent/', views.confirm_payment_intent),
 path('cancel_subscription_p/', views.CancelSub_FP), 
 path('cancel_subscription_t/', views.CancelSub_C),

]
