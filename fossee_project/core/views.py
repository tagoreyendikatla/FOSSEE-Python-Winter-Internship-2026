from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import EventUploadForm
from .models import EventUpload

# Create your views here.

#home
def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'core/home.html')

# Registration
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created successfully!")
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form':form})

#login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})

#profile
@login_required
def profile(request):
    user_uploads = EventUpload.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'core/profile.html', {'uploads':user_uploads})

#upload
@login_required
def upload(request):
    if request.method == 'POST':
        form = EventUploadForm(request.POST, request.FILES)
        if form.is_valid():
            event_instance = form.save(commit=False)
            event_instance.user = request.user
            event_instance.save()
            messages.success(request, "Your file has been uploaded successfully!")
            return redirect('profile')
    else:
        form = EventUploadForm()
    return render(request, 'core/upload.html', {'form':form})

#logout
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')