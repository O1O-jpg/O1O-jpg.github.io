def a_function():
    print("--- A_function ---")

def b_function():
    a_function()
    print("--- B_function ---")

def c_function():
    b_function()
    print("--- C_function ---")

c_function()
