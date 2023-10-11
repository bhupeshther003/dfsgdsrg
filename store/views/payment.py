from django.shortcuts import render, redirect
from store.models.payment_model import *
from django.utils import timezone
from store.models.customer import Customer
from django.views import View
from django.core.mail import send_mail
import uuid

class Payment(View):
    def get(self, request):
        customer = request.session.get('customer')
        return render(request, 'payments.html')
 
    def post(self, request):
        postData = request.POST
        card_number = postData.get('card')
        expiration_date = postData.get('month')
        cvv = postData.get('cvv')
        card_holder_name = postData.get('name')
       
        # Validation
        value = {
            'card_number': card_number,
            'expiration_date': expiration_date,
            'cvv': cvv,
            'card_holder_name': card_holder_name
        }
        error_message = None

        payment = Paymentmod(
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            card_holder_name=card_holder_name
        )
        error_message = self.validatepayment(payment)
       
        
       
        if not error_message:
            print(card_number, expiration_date, cvv, card_holder_name)
            transaction_id = uuid.uuid4()
            payment.transaction_id = transaction_id
            payment.save()  # Save the instance to the database
            customer_id = request.session.get('customer')
            customer = Customer.objects.get(id=customer_id)
            send_mail(
                subject=f'Message from InnerUplift - Transaction Successful',
                message=f'Thank you for your transaction, {customer.first_name} {customer.last_name}!\n\n'
                        f'We are delighted to inform you that your recent transaction was successful. Below are the details:\n\n'
                        f'Transaction ID: {transaction_id}\n'
                        f'Card Number: XXXX-XXXX-XXXX-{card_number[-4:]}\n'
                        f'Card Holder Name: {card_holder_name}\n'
                        f'Transaction Date: {timezone.now().date()} \n\n\nYour treasure awaits! \n\n\n\n Warm regards, \n Inner Uplift \n bhupeshther5@gmail.com \n +91 7378417908 \n',
                         
                from_email='bhupeshther5@gmail.com',  # Replace with your email
                recipient_list={customer.email},
                        
                fail_silently=False,
               )
            return redirect('orders')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'payments.html', data)

    def validatepayment(self, payments):
        error_message = None
        if  (not payments.card_number):
            error_message = "Please Enter your Card Number !!"
        elif len (payments.card_number) == 17:
            error_message = 'Card Number must be  16 Numbers !!'
        elif not payments.expiration_date:
            error_message = 'Please Enter your Expiration Date'
        elif len (payments.expiration_date) == timezone.now().date():
            error_message = 'expiration_date must be current date or future only'
        elif not payments.cvv:
            error_message = 'Enter your cvv '
        elif len (payments.cvv) < 3:
            error_message = 'cvv must be 3 char Long'
        elif ( not payments.card_holder_name):
            error_message = 'Please Enter your Card Holder Name !!'
        elif len(payments.card_holder_name) < 3 :
            error_message = 'Card Holder Name must be 3 char long or more'
        
        # saving
        return error_message
    




class Payment_upi_id(View):
    def get(self, request):
        customer = request.session.get('customer')
        return render(request, 'payments.html')
 
    def post(self, request):
        postData = request.POST
        upi_id = postData.get('uip_id')
        password  = postData.get('password_upi')
       
       
        # Validation
        value = {
            'upi_id': upi_id,
            'password': password,
        }
        error_message = None

        payment = Paymentmod_upi(
            upi_id=upi_id,
            password=password,
        )
        error_message = self.validatepayment(payment)

        if not error_message:
            transaction_id = uuid.uuid4()
            payment.transaction_id = transaction_id
            payment.save()  # Save the instance to the database
            customer_id = request.session.get('customer')
            customer = Customer.objects.get(id=customer_id)
            send_mail(
                subject=f'Message from InnerUplift - Transaction Successful',
                message=f'Thank you for your transaction, {customer.first_name} {customer.last_name}!\n\n'
                        f'We are delighted to inform you that your recent transaction was successful. Below are the details:\n\n'
                        f'Transaction ID: {transaction_id}\n'
                        f'Upi ID: XXXX-XXXX-XXXX-{upi_id[-5:]}\n'
                        f'UPI Holder Name: {customer.first_name} {customer.last_name}\n'
                        f'Transaction Date: {timezone.now().date()} \n\n\nYour treasure awaits! \n\n\n\n Warm regards, \n Inner Uplift \n bhupeshther5@gmail.com \n +91 7378417908 \n',
                         
                from_email='bhupeshther5@gmail.com',  # Replace with your email
                recipient_list={customer.email},
                        
                fail_silently=False,
               )
            return redirect('orders')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'payments.html', data)

    def validatepayment(self, payments):
        error_message = None
        if  (not payments.upi_id):
            error_message = "Please Enter your Card Number !!"
        elif not payments.password:
            error_message = 'Please Enter your Expiration Date'
        elif len (payments.password) <= 4 :
            error_message = ' Password must be 4 char long or more '
        # saving
        return error_message