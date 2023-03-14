import os
import environ
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from portfolio.settings import BASE_DIR
from .models import Portfolio

# open .env
env = environ.Env(DEBUG=(bool, False))
env.read_env(os.path.join(BASE_DIR, '.env'))

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        today = datetime.today()
        today = today.strftime("%Y/%m/%d")
        now = datetime.now()
        now = now.strftime("%Y/%m/%d %H:%M:%S")
        # Send email to me
        email_to_me = EmailMessage(
            subject=f'{now} Portfolioサイトからのメッセージ',
            body=f'以下の問い合わせ発生。\n Name: {name} \n Email: {email}  \
                \n Phone: {phone} \n Message: {message} \n Date: {now}',
            from_email=env("EMAIL_HOST_USER"),
            to=[env("EMAIL_HOST_USER")]
        )
        email_to_me.send(fail_silently=False)

        # Send email to customer
        email_to_customer = EmailMessage(
            subject=f'{today} Thank you for your message',
            body=f'Hi {name} \n Thank you for your message. \
                Yakrk will be contacting you shortly.',
            from_email=env("EMAIL_HOST_USER"),
            to=[email],
            reply_to=[env("EMAIL_HOST_USER")],
            bcc=[env("EMAIL_HOST_USER")],
        )
        email_to_customer.send(fail_silently=False)
        messages.success(
            request, "Your inquiry has been submitted.")
        return redirect('{}#contact'.format(reverse('index')))
    else:
        portfolios = Portfolio.objects.order_by("-created_date").filter(is_published=True)
        context = {
            "portfolios": portfolios
        }
    return render(request, "pages/top.html", context)
