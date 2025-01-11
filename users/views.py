from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
  # If form submitted
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # save user
      form.save()
      return redirect("posts:list")
  else:
    form = UserCreationForm()
  return render(request, 'users/register.html', {"form": form})