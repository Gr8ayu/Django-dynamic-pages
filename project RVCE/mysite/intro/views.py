from django.contrib.auth import login, authenticate
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib import messages
from .forms import SignUpForm
from django.views.generic import DetailView, ListView
from .models import branch , Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@login_required
def index(request):
    return render(request, 'intro/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('intro:homepage')
    else:
        form = SignUpForm()
    return render(request, 'intro/signup.html', {'form': form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))  # removed _ from ('you...
            return redirect('intro:homepage')
        else:
            messages.error(request, ('Please correct the error below.'))  # removed _ from ('Pleas...
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class BranchList(ListView):
    template_name = 'intro/branchlist.html'

    def get_queryset(self):
        return branch.objects.all()


class BranchDetail(DetailView):
    model = branch
    template_name = 'intro/branchdetail.html'


@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    template_name = 'intro/studentlist.html'

    def get_queryset(self):
        return Profile.objects.all()