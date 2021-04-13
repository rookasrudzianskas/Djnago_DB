from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


# Create your views here.

def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {
        'all': all_members
    })


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, "Your form has been submitted successfully!")
        return redirect('home')

    else:
        return render(request, 'join.html', {

        })
