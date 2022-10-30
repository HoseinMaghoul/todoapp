from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        full_name = request.POST['full_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'this email alredy exists')
                return redirect('accounts:user_register')
            elif User.objects.filter(username = username).exists():
                messages.error(request, 'this username alredy exists')
                return redirect('accounts:user_register')
            else:
                user = User.objects.create_user(username=username, email=email, full_name=full_name)
                user.save()




        else:
            messages.error('password must mached!')
            return redirect('accounts:user_register')
    else:
        return render(request, 'accounts/user_register.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'login sucessfuly')
            return redirect('todolist:home')

    else:
        return render(request, 'accounts/login.html')


def profile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account:profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'account/profile.html', context)
