from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from django.shortcuts import render

from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)
    return render(request, 'listings/band_detail.html',{'band': band})

def about(request):
    return render(request, 'listings/about-us.html')

def annonces_list(request):
    lists = Listing.objects.all()
    return render(request, 'listings/annonces_list.html', {'lists': lists})

def annonce_detail(request, annonce_id):
    annonce = Listing.objects.get(id = annonce_id)
    return render(request, 
                'listings/annonce_details.html',
                {'annonce': annonce})

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')

    else: # GET
        form = ContactUsForm()
    
    return render(request,
                'listings/contact.html',
                {'form': form}) 

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def about(request):
    return render(request, 'listings/about.html')

def band_create(request):
    return render(request, 'listings/band_create.html')