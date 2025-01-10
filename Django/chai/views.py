from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ChaiVariety, ChaiStore
from .forms import ChaiVarityForm

# Create your views here.

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai_detail.html', {'chai':chai})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
           chai_variety = form.cleaned_data['chai_varity']
           stores = ChaiStore.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()       

    return render(request, 'chai_stores.html', {'stores' : stores, 'form' : form})
    
