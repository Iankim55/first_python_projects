x = 50  # Global variable

def outer():
    x = 20  # Enclosing variable

    def inner():
        x = 10  # Local variable
        print(x)  # Refers to the local x

    inner()

outer() # Output: 10
print(x)  # Output: 50 (global x)