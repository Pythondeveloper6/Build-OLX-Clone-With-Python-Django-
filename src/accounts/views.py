from django.shortcuts import render , redirect

from .forms import UserForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/products')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'registration/register.html' , context)