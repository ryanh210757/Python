name = "dave"
count = 1







def another():
    color = "blue"
    global count 
    count += 3
    print(count)
    def greeting(name):
        nonlocal color
        color = "green"
        print(name)
        print(color)
    greeting("Dave")

another()
