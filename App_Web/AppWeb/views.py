from django.shortcuts import render
from .models import Product, Wallpaper, Avatar
from django.http import HttpResponse
from .forms import UserRegistrationForm, ProductForm, ImageForm
from django.shortcuts import render, get_object_or_404, redirect
#class-based view invocations
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
#we invoke the log in form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
#---- request log in
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "BASE.html", { "url": avatar.image.url})
    except:
        return render(request, "BASE.html")
        raise


@login_required
def wallpapers(request):
    images = Wallpaper.objects.all()
    return render(request, 'wallpapers.html', {"images": images})


@login_required
def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'details.html', {'product': product})

def memeros(request):
    products = Product.objects.all()
    return render(request, "memeros.html", {'products': products})

def profile(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "profile.html",{ "url": avatar.image.url})
    except:
        return render(request, "profile.html")
        raise

def ask_log(request):
    try:    
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "requestLogIn.html",{ "url": avatar.image.url})
    except:
        return render(request, "requestLogIn.html")
        raise

@login_required
def store(request):
    products = Product.objects.all()
    return render(request, "MemeStore.html", {'products': products})

@login_required
def tetris(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "GAME-1.html",{ "url": avatar.image.url})
    except:
        return render(request, "GAME-1.html")
        raise
@login_required
def bobble(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "GAME-2.html",{ "url": avatar.image.url})
    except:
        return render(request, "GAME-2.html")
        raise

def fail(request):
    return render(request, "404.html")
@login_required
def sokoban(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "GAME-3.html",{ "url": avatar.image.url})
    except:
        return render(request, "GAME-3.html")
        raise

def fail(request):
    return render(request, "404.html")

#--------------LOG IN--------------------

def login_usuario(request):
    try:
        if request.method == "POST":
            miformulario = AuthenticationForm(request, data=request.POST)
            if miformulario.is_valid():
                data = miformulario.cleaned_data
                usuario = data["username"]
                psw = data["password"]   
                user = authenticate(username=usuario, password=psw)
                if user:
                    try:
                        login(request, user)
                        avatar = Avatar.objects.get(user=request.user.id)
                        return render(request, "BASE.html",{ "url": avatar.image.url})
                    except:
                        return render(request, "BASE.html")
                        raise
                else:
                    return render(request, "failLogin.html", {"mensaje": "Error: Incorrect data, you will be terminated"})                         
            else:
                return render(request, "failLogin.html", {"mensaje": "incorrect data"})
        else:
            miformulario = AuthenticationForm()        
            return render(request, "login.html",{"miFormulario": miformulario})
    except:
        return render(request, "BASE.html")
        raise

#--------------REGISTER--------------------

def register(request):
    try:
        if request.method == "POST":
            miformulario = UserRegistrationForm(request.POST)
            if miformulario.is_valid():
                data = miformulario.cleaned_data
                username = data["username"]
                password = data["password1"]
                user = miformulario.save(commit=False)
                user.set_password(password)
                user.save()
                return render(request, "SuccessRegistry.html", {"mensaje": f"Usuario: {username}"})               
            else:
                return render(request, "failRegistry.html", {"mensaje": "Formulario invalido"})
        else:
            miformulario = UserRegistrationForm()        
            return render(request, "Register.html",{"miFormulario": miformulario})
    except:
        return render(request, "Register.html",{"miFormulario": miformulario})
        raise

#-------------- PRODUCT ------------
@login_required
def reg_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'Register_product.html', {'form': form})


def detail_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'details.html', context)


def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


#-------------- Images ------------

@login_required
def up_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('wallpapers')
    else:
        form = ImageForm()
    return render(request, 'uploadImage.html', {'form': form})


#----- Funcion de busqueda ----------------

def search_images(request):
    if request.method == 'GET':
        query = request.GET.get('searchKeyword')
        results = Wallpaper.objects.filter(name__icontains=query)
        context = {'results': results}
        return render(request, 'search_results.html', context)
    
#----------------------------------------

#-------------- Avatar ------------


def start_avatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, 'BASE.html', {'url':avatar[0].image.url})
