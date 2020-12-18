import stripe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['POST'])
def confirm_payment_intent(request):
    data = request.data
    payment_intent_id = data['payment_intent_id']

    stripe.PaymentIntent.confirm(payment_intent_id)

    return Response(status=status.HTTP_200_OK, data={"message": "Success"})


@api_view(['POST'])
def save_stripe_info(request):
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

    # creando paymentIntent

    stripe.PaymentIntent.create(customer=customer,
                                payment_method=payment_method_id,
                                currency='pln', amount=1500,
                                confirm=True)

    # creando una suscripón

    stripe.Subscription.create(
        customer=customer,
        items=[
            {
                'price': 'prod_IT81gH6zCKsz4q'
            }
        ]
    )

    return Response(status=status.HTTP_200_OK, data={'message': 'Success', 'data': {'customer_id': customer.id,
                                                                                    'extra_msg': extra_msg}})
