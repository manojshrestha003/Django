from django.shortcuts import render, HttpResponse
from myapp.models import Contact

# Create your views here.

def index(request):
    context = {
        "variable": "Manoj Shrestha"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This  is Home Page")

def about(request):
    # return HttpResponse("This  is about Page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This  is services Page")
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')

        # Save the form data to the database
        contact = Contact(email=email, password=password, address1=address1, address2=address2, city=city)
        contact.save()

        # Pass a success message to the template
        return render(request, 'contact.html', {"message": "Your details have been submitted successfully!"})

    # Handle GET request
    return render(request, 'contact.html')
