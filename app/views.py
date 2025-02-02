from django.shortcuts import render
from .models import Shop
# Create your views here.
def shop_list(request):
    category = request.GET.get('category')

    if category:
       shops = Shop.objects.filter(category=category)
    else: 
       shops = Shop.objects.all()

    return render(request, 'shop_list.html', {'shops': shops})

def index(request):
   return render(request, 'index.html')

def signup(request):
   return render(request, 'signup.html')

def login(request):
   return render(request, 'login.html')

def shop(request):
   return render(request, 'shop.html')

def chat(request):
   return render(request, 'chat.html')