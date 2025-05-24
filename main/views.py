from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
    
def download(request):
    return render(request, 'main/download.html')