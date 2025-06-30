# Local Variable : Variable we declared inside the function is called local variable.
                  # The scope of variable is limited to function only.
# Global variable : Variable we declared outside the function is called global variable.
                  # The scope of variable is across tte module, means any function can use it
# Non-Local variable : Non-local variable is defined inside the outer function, that is available
                  # for all the inner function.
                  # The scope of non-local variable is limited to outer function and all inner
                  # function, can not access outside of the inner function.


var_x = 700


def function1():
    print("-----function1-----")
    var_y = 900
    print("global variable var_x :", var_x)
    print(("local variable var_y :", var_y))


def function2():
    print("-----function2-----")
    var_z = 800
    print("global variable var_x :", var_x)
    print(("local variable var_z :", var_z))


function1()
function2()
# -----function1-----
# global variable var_x : 700
# ('local variable var_y :', 900)
# -----function2-----
# global variable var_x : 700
# ('local variable var_z :', 800)


print("-"*50)
var_p = 100


def outer_fun():
    var_q = 200

    def inner_fun1():
        global var_p
        nonlocal var_q
        print("---------Inner Function 1----------")
        var_r = 300
        var_p = 1000
        var_q = 2000
        print("Global variable var_p :", var_p)
        print("Non local variable var_q :", var_q)
        print("Local variable var_r:", var_r)

    def inner_fun2():
        print("---------Inner Function 1----------")
        var_s = 400
        print("Global variable var_p :", var_p)
        print("Non local variable var_q :", var_q)
        print("Local variable var_s:", var_s)

    inner_fun2()
    print("-"*50)
    inner_fun1()
    print("-"*50)
    inner_fun2()


outer_fun()
# ---------Inner Function 1----------
# Global variable var_p : 100
# Non local variable var_q : 200
# Local variable var_s: 400
# --------------------------------------------------
# ---------Inner Function 1----------
# Global variable var_p : 1000
# Non local variable var_q : 2000
# Local variable var_r: 300
# --------------------------------------------------
# ---------Inner Function 1----------
# Global variable var_p : 1000
# Non local variable var_q : 2000
# Local variable var_s: 400
