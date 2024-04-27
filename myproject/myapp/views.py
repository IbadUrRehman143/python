from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == "POST":
        print(request.POST.get("name"))
        context = {"name": request.POST.get("name")}
    return render(request, "index.html", context)