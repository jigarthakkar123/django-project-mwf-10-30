global x
x=10

def test1():
    global y
    y=20
    print("X : ",x," Y : ",y)
    y=y+20
def test2():
    print("X : ",x," Y : ",y)


test1()
test2()
