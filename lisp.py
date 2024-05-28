Symbol = str
Number = (int,float)
Atom = (Symbol,Number)
List = list
Sexp = (Atom,List)

#Lexer 
def lexer(input:str) -> List[str]:
    tokenized_input = input.replace( "(","(").replace(")",")").split()
    return tokenized_input

#Parser 
def generate_ast(tokens:List) -> List:
    t = tokens.pop(0)
    if t == "(" :
        ast = []
        while tokens[0] != ")":
            ast.append(generate_ast(tokens))


