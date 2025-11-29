from django.shortcuts import render

def dashboard(request):
    return render(request, "account/user-panel-index.html")
