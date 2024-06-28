from django.shortcuts import render

# Create your views here.
def chat1(request):
    return render(request,'chat1.html')

def chat2(request):
    return render(request,'chat2.html')
