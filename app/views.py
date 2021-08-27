from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from .forms import UserForm
from .models import UserProfile
from django.template import loader, Context
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist


@login_required
@require_http_methods(["GET"])
def user_view(request):
    user=request.user
    if request.method == 'GET':
        queryset = UserProfile.objects.all().filter(username=user)
        for a in queryset:
            print(a.address)
        return render(request, 'user_view.html', {'data': queryset})


@login_required
@require_http_methods(["GET", "POST"])
def user_edit(request):
    user=request.user
    data = {}
    data['form'] = UserForm()
    form = UserForm(request.POST or None)
    form.is_valid()
    if request.method == 'POST':
        try:
            user = UserProfile.objects.get(username=user)
        except ObjectDoesNotExist:
            return HttpResponse("wrong user", status=400)
        user.address = form.cleaned_data['address']
        user.salary = form.cleaned_data['salary']
        user.save()
        return HttpResponse("updated successfully", status=200)
    else:
        print("something went wrong, cannot update user")
    return render(request, "user_edit.html", data)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


@login_required
def admin_view(request, id):
    user = request.user
    if user.is_superuser == True:
        if request.method == 'GET':
            queryset=UserProfile.objects.all()
            return render(request, 'admin_view.html', {"data": queryset})
        if request.method == 'DELETE':
            queryset= UserProfile.objects.get(user=id)
            queryset.delete()
            return HttpResponse("deleted successfully", status=200)
