def KFC():
    num = int(input())
    return num

def BBQ():

    if KFC() > 5:
        return '만세'
    else:
        return '다시'

print( BBQ() )
