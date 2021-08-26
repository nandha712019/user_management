from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import UserForm
from .models import UserProfile


#@login_required
@require_http_methods(["GET", "POST", "UPDATE"])
def user_view(request):
    user=request.user
    form = UserForm(request.POST)
    if request.method == 'GET':
         queryset = UserProfile.objects.all().filter(username=user)
         return render(request, 'user_view.html', {'data': queryset})
    if request.method == 'POST':
        #book = UserProfile.objects.get(username=user)
        if form.is_valid():
            form.save()
            response= redirect('/user_view/')
            #return JsonResponse({"data": "updated successfully"}, safe=False, status=200)
            return response
        if not form.is_valid():
            return JsonResponse({"data": "cannot update something went wrong!"}, safe=False, status=400)
        return render(request, 'user_edit.html', {'form': form})


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
