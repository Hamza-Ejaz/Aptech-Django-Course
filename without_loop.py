# Even & Odd operations from List without using Loop

list_1 = ["a", "b", "c","d", "e","f","g","h","i"]

m = 0

def even():
    global m
    print (list_1[m])
    m = m+2
    try:
        even()
    except:
        print("operation done")

even()