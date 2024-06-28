from django.shortcuts import render

# Create your views here.
def ai(request):
    return render(request,'ai.html')

def ai_tool(request):
    return render(request,'ai_tool.html')
