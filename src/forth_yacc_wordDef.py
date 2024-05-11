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

def p_axioma(p):
    '''axioma   : axioma ponto
                | axioma COMMENT
                | axioma expression
                | axioma definition
                | axioma variable_list
                | empty'''

def p_empty(p):
    '''empty :'''


def p_ponto(p):
    '''ponto : PONTO'''
    valor = stack.pop()
    if valor == "INT":
        assembly_code.append(f'WRITEI')
    elif valor == "FLOAT":
        assembly_code.append(f'WRITEF')


def p_expression_arithmetic(p):
    '''expression : int int operationi
                  | float float operationf
                  | float int operationf
                  | int float operationf
                  '''

    
def p_int(p):
    '''int : INT'''
    assembly_code.append(f'PUSHI {p[1]}')  
    stack.append("INT")
    print(" Push the integer onto the stack")

def p_float(p):
    '''float : FLOAT'''
    assembly_code.append(f'PUSHF {p[1]}')  # Push the float onto the stack
    stack.append("FLOAT")

def p_variable_list(p):
    '''variable_list : int variable_list
                     | float variable_list
                     | int
                     | float'''
    # Handle the case when only variables are inputted

def p_definition(p):
    '''definition : COLON WORD COMMENT code SEMICOLON'''
    defined_words[p[2]] = p[4]  # Store the code for the defined word

def p_code(p):
    '''code : expression'''

def p_operationi_plus(p):
    '''operationi : PLUS'''
    assembly_code.append('ADD')  # Addition operation
    stack.pop()  
    stack.pop()
    stack.append("INT")

def p_operationi_minus(p):
    '''operationi : MINUS'''
    assembly_code.append('SUB')
    stack.pop()  
    stack.pop()
    stack.append("INT")
    print(" Subtraction operation")

def p_operationi_times(p):
    '''operationi : TIMES'''
    assembly_code.append('MUL')  # Multiplication operation
    stack.pop()  
    stack.pop()
    stack.append("INT")
    
def p_operationi_divide(p):
    '''operationi : DIVIDE'''
    assembly_code.append('DIV')  # Division operation
    stack.pop()  
    stack.pop()
    stack.append("INT")

def p_operationi_mod(p):
    '''operationi : MOD'''
    assembly_code.append('MOD')  # Addition operation
    stack.pop()  
    stack.pop()
    stack.append("INT")
    
def p_operationf_plus(p):
    '''operationf : PLUS'''
    assembly_code.append('FADD')  # Addition operation
    stack.pop()  
    stack.pop()
    stack.append("FLOAT")
    
def p_operationf_minus(p):
    '''operationf : MINUS'''
    assembly_code.append('FSUB')  # Subtraction operation
    stack.pop()  
    stack.pop()
    stack.append("FLOAT")
    
def p_operationf_times(p):
    '''operationf : TIMES'''
    assembly_code.append('FMUL')  # Multiplication operation
    stack.pop()  
    stack.pop()
    stack.append("FLOAT")
    
def p_operationf_divide(p):
    '''operationf : DIVIDE'''
    assembly_code.append('FDIV')  # Division operation
    stack.pop()  
    stack.pop()
    stack.append("FLOAT")
                 
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
data = ''': AVERAGE ( a b -- avg ) 2 2 + ;''' 
# data = '''20.0 20 + . ( comentario )'''
parser.parse(data)

# Print the generated assembly code
print("Assembly code:")
for instruction in assembly_code:
    print(instruction)
