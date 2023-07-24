arr = [['F','E','W'],['D','C','A']]

def main():
    ch = input()
    return findCh(ch)
def findCh(ch):
    global arr
    count = 0
    for i in arr:
        for j in i:
            if j == ch:
                count +=1
    if count >=1:
        print('발견')
    else:
        print('미발견')

main()
