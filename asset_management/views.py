from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Asset
from .forms import AssetForm

# Create your views here.
def AssetList(request):
    assets = Asset.objects.all()

    context = {'assets':assets}
    return render(request, 'asset_list.html', context)

def AssetCreate(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    form = AssetForm 
    return render(request, 'asset_create.html', {'form':form})