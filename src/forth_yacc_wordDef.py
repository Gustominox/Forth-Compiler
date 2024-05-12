import ply.yacc as yacc
yacc.debug = True

# Get the token list from the lexer module
from forth_lex import tokens

# Assembly code output
assembly_code = []

# stack de dados
stack = []

# Dictionary to store defined words
defined_words = {}

def p_axioma_iter(p):
    '''axioma : axioma line'''
    p[0] = p[1] + p[2]

def p_axioma_empty(p):
    '''axioma : empty'''
    p[0] = ""

def p_line_comment(p):
    '''line : COMMENT'''
    p[0] = ""
    
def p_line_ponto(p):
    '''line : PONTO'''
    valor = stack.pop()
    if valor == "INT":
        p[0] = f'WRITEI\n'
    elif valor == "FLOAT":
        p[0] = f'WRITEF\n'

def p_line_expression_arithmetic(p):
    '''line : line operation'''
    p[0] = f'{p[1]}{p[2]}'

def p_line_variable_list(p):
    '''line : int line
            | float line''' 
    p[0] = f'{p[1]}{p[2]}'

def p_line_int(p):
    '''line : int'''
    p[0] = p[1]

def p_line_float(p):
    '''line : float'''
    p[0] = p[1]

def p_int(p):
    '''int : INT'''
    stack.append("INT")
    p[0] = f'PUSHI {p[1]}\n'

def p_float(p):
    '''float : FLOAT'''
    stack.append("FLOAT")
    p[0] = f'PUSHF {p[1]}\n'


def p_line_definition(p):
    '''line : COLON WORD COMMENT code SEMICOLON'''
    p[0] = f'{p[2]}:\n{p[4]}'
    
def p_code(p):
    '''code : axioma'''
    p[0] = p[1]
    
def p_line_word(p):
    '''line : WORD'''
    if p[1] in defined_words:
        assembly_code.append(defined_words[p[1]])  # Compile the code associated with the word
    else:
        print("Undefined word:", p[1])

def p_operation_plus(p):
    '''operation : PLUS'''
    val1 = stack.pop()  
    val2 = stack.pop()
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FADD\n'
    else:
        stack.append("INT")
        p[0] = f'ADD\n'
    

def p_operation_minus(p):
    '''operation : MINUS'''
    val1 = stack.pop()  
    val2 = stack.pop()
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FSUB\n'
    else:
        stack.append("INT")
        p[0] = f'SUB\n'


def p_operation_times(p):
    '''operation : TIMES'''
    val1 = stack.pop()  
    val2 = stack.pop()
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FMUL\n'
    else:
        stack.append("INT")
        p[0] = f'MUL\n'
    
def p_operation_divide(p):
    '''operation : DIVIDE'''
    val1 = stack.pop()  
    val2 = stack.pop()
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FDIV\n'
    else:
        stack.append("INT")
        p[0] = f'DIV\n'

def p_operationi_mod(p):
    '''operation : MOD'''
    val1 = stack.pop()  
    val2 = stack.pop()
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        print("Operacao impossivel com floats")
    else:
        stack.append("INT")
        p[0] = f'MOD\n'
                 
def p_empty(p):
    'empty :'
    pass

        
def p_error(p):
    if p:
        print("Syntax error at line", p.lineno, "column", find_column(data, p))
    else:
        print("Syntax error: unexpected end of input")

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Build the parser
parser = yacc.yacc()

# Test the parser
# data = ''': AVERAGE ( a b -- avg ) + 2/ ;''' 
data = '''30 5 + 7 / .'''

r = parser.parse(data)

# Print the generated assembly code
print(r)
