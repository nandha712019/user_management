from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EmployeeForm
from .models import UserModel


@login_required
@require_http_methods(["GET", "POST"])
def user_view(request):
    user=request.user
    # if request.method == 'GET':
    #     queryset = UserModel.objects.all().filter(name=user)
    #     return render(request, 'user_view.html', {'data': queryset})
    if request.method == 'POST':
        book = get_object_or_404(UserModel, name=user)
        form = EmployeeForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('accounts/logout')
        #     return JsonResponse({"data": "updated successfully"}, safe=False, status=200)
        # if not form.is_valid():
        #     return JsonResponse({"data": "cannot update something went wrong!"}, safe=False, status=400)
        return render(request, 'user_edit.html', {'form': form})
