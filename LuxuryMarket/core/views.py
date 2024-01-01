# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from multiprocessing import context
from django.views.generic import TemplateView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse
from .models import Profile
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}! Your account has been created! Now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile.html', context)

class TermsAndConditionsView(TemplateView):
    template_name = 'terms-and-conditions.html'

def user_search(request):
    query = request.GET.get('q', '')
    results = User.objects.filter(username__icontains=query)
    return render(request, 'user_search.html', {'results': results, 'query': query})

@login_required
def user_profile(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)
    context = {'user_profile': user_profile}
    return render(request, 'profile_view_for_other_users.html', context)

@login_required
@require_POST
def follow_unfollow(request, username):
    user_profile = get_object_or_404(Profile, user__username=username)

    if request.user.profile in user_profile.followers.all():
        user_profile.followers.remove(request.user.profile)
        messages.success(request, f'You unfollowed {user_profile.user.username}.')
    else:
        user_profile.followers.add(request.user.profile)
        messages.success(request, f'You are now following {user_profile.user.username}.')

    return redirect(reverse('core:user_profile', kwargs={'username': username}))