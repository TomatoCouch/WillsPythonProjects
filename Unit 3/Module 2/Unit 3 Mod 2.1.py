#Will C.
#Python 1
#Unit 3, Mod 2.1

#Task 1
# [ ] Use relational and/or arithmetic operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. x >= y)
# 3 expressions that evaluate to False (i.e. x <= y)
x = 84
y = 17
x=y
y=x
type(x)==str
x!=y
y!=x
type(x+y)==int

# [ ] Use the basic Boolean operators with the variables x and y to write:
# 3 expressions that evaluate to True (i.e. not y)
# 3 expressions that evaluate to False (i.e. x and y)
x = True
y = False
not y
x
x!=y
not x
y
x=y

# [ ] Write an expression to test if x is an even number outside the range [-100, 100]
x=-99
if x<-100 or x>100:
    print("True")
else:
    print("False")
# Test your expression with:
# x = 104 (True)
# x = 115 (False)
# x = -106 (True)
# x = -99 (False)

s="CapitaL"
# [ ] Write an expression to test if a string s starts and ends with a capital letter
if s[0].isupper()==True and s[-1].isupper()==True:
    print("True")
else:
    print("False")
# HINT: You might find the function `str.isupper()` useful
# Test your expression with
# s = "CapitaL" (True)
# s = "Not Capital" (False)

s="39"
x=24
num=""
# [ ] Write an expression to test if a string s contains a numerical value
if s.isnumeric()==True:
    if int(s)>x:
        print("True")
    else:
        print("False")
else:
    print("False")
# then test if the value is greater than the value stored in x
# HINT: Use the functions `s.isnumeric()` and `float(s)`
# Test your expression with
# s = "39"
# x = 24
# Expression should yield True
# s = "a39"
# x = 24
# Expression should yield False