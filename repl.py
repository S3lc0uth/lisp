import readline
import lisp_readline

def READ(str):
    return str 

def EVAL(ast):
    return ast

def PRINT(exp):
    return exp

def REP(input):
        return(READ(EVAL(PRINT(str))))
    

while True:
        try:
            inp = print(input("User> "))
            REP(inp)
        
        except  EOFError : break





    
    
    


    