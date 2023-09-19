from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'calculators/throw.html')
def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    context = {
        'message1' : message1,
        'message2' : message2
    }
    return render(request, 'calculators/catch.html', context)