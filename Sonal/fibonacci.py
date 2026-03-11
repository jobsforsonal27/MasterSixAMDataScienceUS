def fibonacci(n):
    """ This function returns the fibonacci series upto n terms """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        #a, b = b, a + b  #Pythonic swap method
        a=b
        b = a + b
    return series
print(fibonacci(10))
