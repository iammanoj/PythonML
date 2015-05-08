#!/Users/manoj_mohan/anaconda/bin/python

prices = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
    }
    
stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
    }
    #print prices
    
for key in prices:
        print key
        print "price: ",  prices[key]
        print "stock: ",  stock[key]
