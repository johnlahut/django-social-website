from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.


# User view should follow these steps:
# 1. Get username and password via a form
# 2. Auth the user against the database
# 3. Check to make sure the user is active
# 4. Log the user into the website successfully

def user_login(request):

    # form was submitted
    if request.method == 'POST':

        # get the data from the form that was submitted i.e. instantiate the form
        form = LoginForm(request.POST)

        # check if form is valid, else display errors in the template
        if form.is_valid():

            cleaned_data = form.cleaned_data

            # authenticate the user, returns None if the user could not be authenticated
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            # make sure the user is active
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled account. Contact your site administrator.')

            else:
                return HttpResponse('Invalid login')

    # GET request i.e. display the form
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})