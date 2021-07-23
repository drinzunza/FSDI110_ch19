from data import data

# list of dictionaries
products = data


def test1():
    print("**Print each product title")
    for prod in products:        
        print(prod["title"])


def test2():
    print("-- Sum of all prices")

    sum = 0
    for prod in products:
        price = prod["price"]
        sum += price
    
    print(f"The sum is: {sum}")


def test3():
    print("Products with prices over $13")

    for prod in products:
        if(prod["price"] > 13):
            print(prod["title"])


def test4():
    print("-- total stock value")

    sum = 0
    for prod in products:
        val = prod["price"] * prod["stock"]
        sum += val

    print(f"The value of the stock is: {sum}")



def test5():
    print("** unique categosries")
    
    unique_categories = []
    for prod in products:
        cat = prod["category"]

        # how to check if an element exist inside a list in python
        if cat not in unique_categories:
            unique_categories.append(cat)
            print(cat)
        


def run_tests():
    print("**Starting tests")

    test1()
    test2()
    test3()
    test4()
    test5()


run_tests()



# test 5
# get the list of unique categories
# print each string in the list