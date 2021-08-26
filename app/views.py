from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import UserForm
from .models import UserModel


@login_required
@require_http_methods(["GET", "POST", "UPDATE"])
def user_view(request):
    user=request.user
    if request.method == 'GET':
         queryset = UserModel.objects.all().filter(name=user)
         return render(request, 'user_view.html', {'data': queryset})
    if request.method == 'POST':
        book = UserModel.objects.get(name=2)
        form = UserForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return JsonResponse({"data": "updated successfully"}, safe=False, status=200)
        if not form.is_valid():
            return JsonResponse({"data": "cannot update something went wrong!"}, safe=False, status=400)
        return render(request, 'user_edit.html', {'form': form})
