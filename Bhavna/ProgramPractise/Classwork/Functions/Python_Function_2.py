# 26/06/2025 session continue

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
var_a = 700

def function1():
    print("--------Function1----------")
    var_b = 900 #local variable
    print("global variable var_a:",var_a)
    print("local variable var_b:",var_b)

def function2():
    print("---------Function2---------")
    var_c = 800 #local variable
    print("global variable var_a:",var_a)
    print("local variable var_c:",var_c)

function1()
function2()

var_p = 100 #global variable

def outer_funct():
    var_q = 50 #non local variable

    def inner_funct1():
        global var_p
        nonlocal var_q
        print("----------------inner function1---------")
        var_r = 300 #local variable
        print("global variable var_p:",var_p)
        print("non local variable var_q:",var_q)
        print("local variable var_r:",var_r)

    def inner_funct2():
        print("---------------inner function2----------")
        var_s = 400
        print("global variable var_p:", var_p)
        print("non local variable var_q:", var_q)
        print("local variable var_s:", var_s)

    inner_funct1()
    print('_'*70)
    inner_funct2()
    print('_'*70)

outer_funct()