"""
local variable :  Variable we declare inside the function is called local variable, the scope of local variable
                  is limited to function only
global variable :  variable we declare outside of the functions is called global variable, the scope of variable
                  is across the module, means any function can use it.
non-local variable :  non local variable is defined inside the outer function, that is available for all the inner
                   function, the scope non local variable is limited to outer function and all inner function, can
                   not access outside of the inner function.
"""

# global variable
var_x = 700

def function1():
    print("------function1-------")
    var_y = 900 # local variable
    print("global variable var_x :", var_x)
    print("local variable var_y :", var_y)


def function2():
    print("------function1-------")
    var_z = 800 # local variable
    print("global variable var_x :", var_x)
    print("local variable var_z :", var_z)

function1()
function2()


var_p = 100 # global variable

def outer_func():
    var_q = 200 #non local variable

    def inner_fun1():
            global var_p
            nonlocal var_q
            print("---------  inner function1 ------")
            var_r = 300  # local variable
            var_p = 1000
            var_q = 2000
            print("global variable var_p :", var_p)
            print("non local variable var_q :", var_q)
            print("local variable var_r:", var_r)

    def inner_fun2():
            print("---------  inner function2 ------")
            var_s = 400
            print("global variable var_p :", var_p)
            print("non local variable var_q :", var_q)
            print("local variable var_s:", var_s)


    inner_fun2()
    print("_" * 24)
    inner_fun1()
    print("_" * 24)
    inner_fun2()

outer_func()