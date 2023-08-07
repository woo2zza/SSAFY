def abc(level):
    if level ==2:
        return

    for i in range(2):
        print('#', end = '')
        abc(level + 1)
        print('#', end = '')

abc(0)