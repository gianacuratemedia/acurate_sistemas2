import stripe
from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .permissions import IsOwner
from .models import StripeCustomer
from Usuarios_k.models import User


stripe.api_key='sk_test_51HsBSREnWktr8a8ZgMg3sYI7q46FZ9JklEXbWi0XXUm7FlfqQ1JzeBp082sj4PYn4OkyQEsgwbm95W5VCDJEEJv500tkmNuLvs'

#Test de funcionamiento
@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000,
        currency='pln',
        payment_method_types=['card'],
        receipt_email='test@example.com',
    )

    return Response(status=status.HTTP_200_OK, data=test_payment_intent)

#Crear payment method 

@api_view(['POST'])
def payment_method(request):
    data=request.data
    number=data['number']
    exp_month=data['exp_month']
    exp_year=data['exp_year']
    cvc=data['cvc']

    payment_method_intent=stripe.PaymentMethod.create(
    type="card",
    card={
    "number":number,
    "exp_month":exp_month,
    "exp_year":exp_year,
    "cvc":cvc
    }
 )
    return Response(status=status.HTTP_200_OK, data= payment_method_intent)


#Confirmar pago 

@api_view(['POST'])
def confirm_payment_intent(request):
    data = request.data
    payment_intent_id = data['payment_intent_id']

    stripe.PaymentIntent.confirm(payment_intent_id)

    return Response(status=status.HTTP_200_OK, data={"message": "Success"})



#Suscripción al plan premium anual 

class save_stripe_info_pa(generics.GenericAPIView):
   permission_classes = (permissions.IsAuthenticated,)

   def post(self, request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    extra_msg = ''
    # comprobar si el cliente con el correo electrónico proporcionado ya existe
    customer_data = stripe.Customer.list(email=email).data
    print(customer_data)

    if len(customer_data) == 0:
        # creando un cliente
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
    else:
        customer = customer_data[0]
        extra_msg = "El cliente ya existe"


    # creando una suscripción

    subscription=stripe.Subscription.create(
        customer=customer,
        items=[
            {
                'price': 'price_1HsBnIEnWktr8a8Z6kNBj5hV'
            }
        ]
    )

    #creando un nuevo Stripe Customer
    user = User.objects.get(id=self.request.user.id)
    StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=customer.id,
            stripeSubscriptionId=subscription.id,
            active=subscription.active,
        )  
   

    return Response(status=status.HTTP_200_OK, data={'message': 'Success', 'data': {'customer_id': customer.id,
                                                                                    'extra_msg': extra_msg}})


#Suscripción al plan mensual 
class save_stripe_info_pm(generics.GenericAPIView):
 permission_classes = (permissions.IsAuthenticated,)
 def post(self, request):
    data = request.data
    email = data['email']
    payment_method_id = data['payment_method_id']
    extra_msg = ''
    # comprobar si el cliente con el correo electrónico proporcionado ya existe
    customer_data = stripe.Customer.list(email=email).data
    print(customer_data)

    if len(customer_data) == 0:
        # creando un cliente
        customer = stripe.Customer.create(
            email=email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
    else:
        customer = customer_data[0]
        extra_msg = "El cliente ya existe"


    # creando una suscripción

    subscription=stripe.Subscription.create(
        customer=customer,
        items=[
            {
                'price': 'price_1HsBe5EnWktr8a8ZceHzF4cW'
            }
        ]
    )

    #creando un nuevo Stripe Customer
    user = User.objects.get(id=self.request.user.id)
    StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=customer.id,
            stripeSubscriptionId=subscription.id,
            active=subscription.active,
        )  
   

    return Response(status=status.HTTP_200_OK, data={'message': 'Success', 'data': {'customer_id': customer.id,
                                                                                    'extra_msg': extra_msg}})



#Consultar status de suscripción
def my_subs(request):
    try:
        # Retrieve the subscription and product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        return Response(request,  {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        return Response(request, {'La suscripción no existe'})



 #Cancelar suscripción o eliminar suscripción
@api_view(['POST'])
def CancelSub_C(request):
        data=request.data
        subscription_id= data['subscription_id']
        Cancel_subs=stripe.Subscription.delete(
        subscription_id
        )
        return Response(status=status.HTTP_200_OK, data=Cancel_subs)

 #Cancelar suscripción al final del periodo de facturación

@api_view(['POST'])
def CancelSub_FP(request):
    data=request.data
    subscription_id= data['subscription_id']
    Cancel_subs=stripe.Subscription.delete(
        subscription_id,
        cancel_at_period_end=True
        )
    
    return Response(status=status.HTTP_200_OK, data=Cancel_subs)


