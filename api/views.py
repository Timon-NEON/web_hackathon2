from django.shortcuts import render

def api_docs(request):
    return render(request, 'api/api_docs.html')