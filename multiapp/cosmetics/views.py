from django.shortcuts import render

# Create your views here.
def c_index(request):
    return render(request,'Cosmetics_template/c_index.html')