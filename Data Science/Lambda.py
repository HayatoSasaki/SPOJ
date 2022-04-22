# Simple Example.
price = 1000
tax = lambda x: x*0.3
print(tax(price)) # 300.
 
# List Example.
prices = [100, 500, 10, 25]
print(list(map(lambda x: x*0.3, prices))) # [30.0, 150.0, 3.0, 7.5]
