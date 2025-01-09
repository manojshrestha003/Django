from django.shortcuts import render, HttpResponse
from myapp.models import Contact
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    context = {
        "variable": "Manoj Shrestha"
    }
   
    return render(request, 'index.html', context)

def about(request):
    messages.success(request, "This is a success message!")
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')

        # Validate form inputs
        if not email or not password or not address1 or not city:
            messages.error(request, "All required fields must be filled out.")
        else:
            # Validate email format
            try:
                validate_email(email)
                # Save data to the database
                contact = Contact(email=email, password=password, address1=address1, address2=address2, city=city)
                contact.save()
                messages.success(request, "Message has been sent successfully.")
            except ValidationError:
                messages.error(request, "Enter a valid email address.")

    return render(request, 'contact.html')
