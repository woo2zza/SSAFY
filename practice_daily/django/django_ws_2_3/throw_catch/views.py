from django.shortcuts import render

# Create your views here.
def throw(request):
    str = request.GET.get('str')
    context = {
        'str' : str
    }
    return render(request, 'throw_catch/throw.html', context)

def catch(request):
    str = request.GET.get('str')
    context = {
        'str' : str
    }
    return render(request, 'throw_catch/catch.html', context)