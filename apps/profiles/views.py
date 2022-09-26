from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm


# Create your views here.
def profile_view(request, pk):
    user = User.objects.get(id=pk)
    form = ProfileForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'profile.html', context)