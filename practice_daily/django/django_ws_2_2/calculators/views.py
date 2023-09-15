from django.shortcuts import render

# Create your views here.
def calculator(request, num, num2):
    context = {
        'num' : num,
        'num2' : num2,
        'mul' : num*num2,
        'mius' : num-num2,
        
    }
    return render(request,'calculators/calculator.html', context)