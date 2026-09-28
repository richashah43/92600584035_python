x = 10     #global

def outer():
    y = 20  #Local to Outer


    def inner():
        nonlocal y
        y = 30
        print("Nonlocal:", y)
        print("Global:",x)


    inner()

outer()

print("Global:",x)
