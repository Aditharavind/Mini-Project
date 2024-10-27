from django.shortcuts import render, redirect
from .models import CEC
from django.contrib.auth.hashers import make_password, check_password

# Homepage view for registration and login page
def homepage(request):
    return render(request, 'login-home/home-page.html')

# Student homepage view
def studenthome(request):
    return render(request, 'login-home/home.html')

# Staff homepage view
def staffhome(request):
    return render(request, 'home.html')

# Register view to handle user registration
def register(request):
    if request.method == 'POST':
        role = request.POST.get('registerRole')
        name = request.POST.get('registerName')
        email = request.POST.get('registerEmail')
        password = request.POST.get('registerPassword')

        if role and name and email and password:
            # Check if email already exists
            if CEC.objects.filter(email=email).exists():
                return render(request, 'login-home/home-page.html', {'error': 'Email already exists'})

            # Save the user
            cec_user = CEC(
                name=name,
                email=email,
                password=make_password(password),  # Hash the password before saving
                role=role
            )
            cec_user.save()

            # Stay on the same page but show a success message
            return render(request, 'login-home/home-page.html', {'message': 'Registration successful!'})
        else:
            return render(request, 'login-home/home-page.html', {'error': 'Please fill all fields'})

    return render(request, 'login-home/home-page.html')


# Login view to handle user authentication
def login(request):
    if request.method == 'POST':
        email = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')

        if email and password:
            try:
                user = CEC.objects.get(email=email)
                if check_password(password, user.password):  # Check if the password matches
                    if user.role == 'staff':
                        # Redirect staff to staff homepage
                        return render(request,'home.html')
                    elif user.role == 'student':
                        # Redirect students to student homepage
                        return render(request,'login-home/home.html')
                    else:
                        # Default success message for other roles (if any)
                        return render(request, 'login-home/home-page.html', {'message': 'Login successful!'})
                else:
                    return render(request, 'login-home/home-page.html', {'error': 'Invalid password'})
            except CEC.DoesNotExist:
                return render(request, 'login-home/home-page.html', {'error': 'Invalid email'})
        else:
            return render(request, 'login-home/home-page.html', {'error': 'Please fill all fields'})

    return render(request, 'login-home/home-page.html')
def viewdata(request):
    return render(request,'table.html')