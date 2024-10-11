import args


def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("ian",)

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_address(street="123 Fake Street",
               city="San Francisco",
               state="CA",)
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    print(f"{kwargs.get('street')}{kwargs.get('city')}{kwargs.get('state')}")
shipping_label("Dr.", "Spongbob",
               street="123 Fake Street",
               city="San Francisco",
               state="CA",)

