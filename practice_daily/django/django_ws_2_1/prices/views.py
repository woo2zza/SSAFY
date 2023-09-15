from django.shortcuts import render

# Create your views here.
def product(request, name, num):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if name in product_price:
        price = product_price[name]
    else:
        price = 0

    context = {
        'price' : price,
        'thing' :name,
        'cnt' : num,
        'product_price': product_price.keys()

    }

    return render(request,'prices/price.html', context)