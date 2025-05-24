from django.shortcuts import render, redirect
from .forms import PartnerApplicationForm

def partner_form(request):
    if request.method == 'POST':
        form = PartnerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_success')
    else:
        form = PartnerApplicationForm()
    return render(request, 'partners/partner_form.html', {'form': form})

def partner_success(request):
    return render(request, 'partners/partner_success.html')