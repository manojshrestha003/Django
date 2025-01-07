from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "Manoj Shrestha"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This  is Home Page ")
def about(request):
   # return HttpResponse("This  is about Page ")
    return render(request, 'about.html')

def services(request):
   # return HttpResponse("This  is services Page ")
     return render(request, 'services.html')
def contact(request):
    #return HttpResponse("<h1>Hello  this is contact page  . pleas contact me  if  you   want </h1>")
     return render(request, 'contact.html')


