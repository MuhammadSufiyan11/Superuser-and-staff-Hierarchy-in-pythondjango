from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib import messages



# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('user_home')  # Redirect to the user's home page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('user_login')
    return render(request, 'login.html')


@login_required
def user_home(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        parent_user = user_profile.parent_user
    except UserProfile.DoesNotExist:
        parent_user = None  # In case no parent user is set

    return render(request, 'user_home.html', {'parent_user': parent_user})

# Register new user view
@login_required
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            UserProfile.objects.create(user=new_user)
            return redirect('user_home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register_user.html', {'form': form})
