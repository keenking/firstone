from django.shortcuts import render

# Create your views here.
def love(requests):
    return render(requests, 'index.html')
