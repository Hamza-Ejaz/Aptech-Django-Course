# return parameters in multiple variables on single line

def biodata (name, age, dob):
    return name, age, dob

n,a,d = biodata("ali", 20 ,"12th jun")
print(n,a,d)