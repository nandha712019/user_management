from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import UserForm, PasswordForm
from .models import UserProfile


@login_required
@require_http_methods(["GET"])
def UserView(request):
    user=request.user
    if request.method == 'GET' and user.is_authenticated == True:
        queryset = UserProfile.objects.all().filter(username=user)
        return render(request, 'user_view.html', {'data': queryset})


@login_required
@require_http_methods(["GET", "POST"])
def UserEdit(request):
    user=request.user
    data = {}
    data['form'] = UserForm()
    form = UserForm(request.POST or None)
    form.is_valid()
    if request.method == 'POST':
        try:
            print('address' in form.changed_data)
            user = UserProfile.objects.get(username=user)
        except ObjectDoesNotExist:
            return HttpResponse("wrong user", status=400)
        if ('address' in form.changed_data) == True:
            user.address = form.cleaned_data['address']
        if ('email' in form.changed_data) == True:
            user.email = form.cleaned_data['email']
        if ('first_name' in form.changed_data) == True:
            user.first_name = form.cleaned_data['first_name']
        if ('last_name' in form.changed_data) == True:
            user.last_name = form.cleaned_data['last_name']
        if ('email' in form.changed_data) == True:
            user.salary = form.cleaned_data['salary']
        user.save()
        return HttpResponse("updated successfully", status=200)
    else:
        print("something went wrong, cannot update user")
    return render(request, "user_edit.html", data)


@login_required
@require_http_methods(["GET"])
def UserList(request):
    user = request.user
    if user.is_superuser == True:
        if request.method == 'GET':
            queryset=UserProfile.objects.all()
            return render(request, 'user_list.html', {"data": queryset})
        else:
            return HttpResponse("request method is wrong", status=400)
    else:
        return HttpResponse("Only admin user is allowed", status=400)


@login_required
@require_http_methods(["GET"])
def UserDelete(request, id):
    user= request.user
    if request.method == 'GET':
        if user.is_superuser == True:
            queryset = UserProfile.objects.get(username=id)
            queryset.delete()
            return HttpResponse("user deleted successfully", status=200)
        else:
            return HttpResponse("Only admin user is allowed", status=400)


@login_required
def password_reset(request):
    data={}
    data['form']=PasswordForm
    if request.method == "POST":
        form = PasswordForm(request.POST or None)
        form.is_valid()
        password=form.cleaned_data['password']
        user = request.user
        query = UserProfile.objects.get(username=user)
        query.set_password(password)
        query.save()
        return HttpResponse("password updated successfully", status=200)
    return render(request, "password_reset.html", data)
