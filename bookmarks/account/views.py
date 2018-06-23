from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):

    # form was submitted
    if request.method == 'POST':

        # get the form data defined in forms.py (form was already submitted and filled out)
        form = UserRegistrationForm(request.POST)

        # validate the form data
        if form.is_valid():

            # instantiate new user
            new_user = form.save(commit=False)

            # use set_password method to safely encrypt and set password
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/regiester_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})


@login_required
def edit(request):

    # form was submitted
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                            data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Error updating your profile')

    # form was requested, render it
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})
