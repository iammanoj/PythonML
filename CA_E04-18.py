#!/Users/manoj_mohan/anaconda/bin/python
import math

intList = [i for i in range(5) if i%2 == 0]

intListS = range(5)
intList3 = [i for i in range(1,15)]

print intList3
print intList3[2:12:2]

print intListS

print (3 ** 2)

c = ['C' for x in range(5) if x < 3]
print c
print range(5)

print "Lambda trial..."

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
for item in movies:
    print item
    #print item, movies.items()
    #print item, movies[item]

list = [x for x in range(6)]
for x in list:
    print bin(x)


my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")
for item in my_list:
    f.write(str(item) + "\n")
f.close()

my_file = open("output.txt","r+")
my_file.write(str("This is my test write") + "\n")
my_file.close()

my_list = [i**2 for i in range(1,11)]
my_file = open("output.txt", "r+")
# Add your code below!
for x in my_list:
    my_file.write(str(x) + "\n")
my_file.close()

my_file = open("text.txt","r")
lines = my_file.readlines()
for line in lines:
    print line
my_file.close()


class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
"""
# Add your Triangle class below!
class Triangle(Shape,s1,s2,s3):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
my_tr = Triangle("MT",1,2,3)
"""

Dictionary = ["cat", "rat", "mat", "sat"]
matrix_indx = math.sqrt(len(Dictionary))
Matrix =[0 for x in range(int(matrix_indx))][ x in range(int(matrix_indx))]
Matrix = Dictionary
print Matrix
"""
print Matrix[0]
print Matrix[1]
print Matrix[2]
print Matrix[3]
print Matrix[0][0]
print Matrix[0][1]
print Matrix[0][2]
print Matrix[1][0]
print Matrix[1][1]
print Matrix[1][2]
print Matrix[0:1]
print Matrix[0:2]
print Matrix[0:3]
print Matrix[0:4]
print Matrix[1:0]
print Matrix[1:1]
print Matrix[1:2]
print Matrix[1:3]
print Matrix[1:4]
print Matrix[:0]
print Matrix[:1]
"""

Str3 = 'sadagobar'
StrR = Str3[::-1]
print StrR

