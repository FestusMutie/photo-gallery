from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
# view is a function that takes the request from a user, processes it and returns a response to the user.



# Create your views here.
def photo(request):
    return render(request,'photos.html')