'''
def greet(name):
    print(f"Hello, {name}")
    
    greet("Melo")
    
    def add(a, b):
        return a + b
    
    result = add(4, 6)
    print(result)
    '''
    
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
        
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
    
    greet("Sihle", "Sawubona")