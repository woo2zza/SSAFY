from django.shortcuts import render
import random
# Create your views here.
def throw(request):
    name = 'woo seok'
    age = random.choice(range(25,31))
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : age,
        'grade' : grade
    }

    return render(request, 'certifications/certification1.html', context)