import re
import ply.yacc as yacc
import sys
import traceback
yacc.debug = True

# Get the token list from the lexer module
from forth_lex import tokens
from forth_lex import defined_words

# Assembly code output
assembly_code = []

# stack de dados
stack = []

# Dictionary to store defined words
#defined_words = {}

if_counter = 0
regist_counter = 0
loop_counter = 1
in_func = False

def p_axioma_iter(p):
    '''axioma : axioma line'''
    p[0] = p[1] + p[2]

def p_axioma_empty(p):
    '''axioma : empty'''
    p[0] = ""

def p_line_comment(p):
    '''line : COMMENT'''
    p[0] = ""
    
def p_line_conditional(p):
    '''line : conditional'''
    p[0] = p[1]

def p_conditional_else(p):
    '''conditional : IF axioma ELSE axioma THEN axioma'''
    global if_counter
    if_counter+=1
    p[0] = f'JZ else{str(if_counter)}\n{p[2]}JUMP endif{str(if_counter)}\nelse{str(if_counter)}:\n{p[4]}endif{str(if_counter)}:\n{p[6]}'

def p_confitional_then(p):
    '''conditional : IF axioma THEN axioma'''
    global if_counter
    if_counter+=1
    p[0] = f'JZ endif{str(if_counter)}\n{p[2]}JUMP endif{str(if_counter)}\nendif{str(if_counter)}:\n{p[4]}'        
    

def p_line_loop(p):
    'line : DO axioma LOOP'
    global regist_counter, loop_counter
    p[0] = f'''
STOREG {str(regist_counter)}
STOREG {str(regist_counter + 1)}
do{str(loop_counter)}:
PUSHG {str(regist_counter + 1)}
PUSHG {str(regist_counter)}
SUB
JZ endDo{str(loop_counter)}
{p[2]}
PUSHG {str(regist_counter)}
PUSHI 1
ADD
STOREG {str(regist_counter)}
JUMP do{str(loop_counter)}
endDo{str(loop_counter)}:
'''
    regist_counter += 2
    loop_counter += 1 
    
def p_line_ponto(p):
    '''line : PONTO'''
    try:
        valor = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '.'\033[0m\n")        
    
    if valor == "INT":
        p[0] = f'WRITEI\n'
    elif valor == "FLOAT":
        p[0] = f'WRITEF\n'

def p_line_cr(p):
    'line : CR'
    p[0] = 'WRITELN \n'
    
def p_line_pontostring(p):
    '''line : PONTOSTRING'''
    p[0] = f'PUSHS {p[1][1:]}\nWRITES\n'

def p_line_emit(p):
    '''line : EMIT'''
    try:
        stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'EMIT'\033[0m\n")     
    
    p[0] = f'WRITECHR\n'

def p_line_char(p):
    '''line : CHAR'''
    letter = p[1][-1]
    stack.append("INT")
    p[0] = f'PUSHI {str(ord(letter))}\n'

def p_line_expression_arithmetic(p):
    '''line : operation'''
    p[0] = p[1]

def p_operation_1plus(p):
    '''operation : 1PLUS'''
    try:
        valor = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '1+'\033[0m\n") 
    
    if(valor == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 1\nADD\n'
    elif(valor == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 1.0\nFADD\n'

def p_operation_1minus(p):
    '''operation : 1MINUS'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '1-'\033[0m\n") 
    
    if(val1 == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 1\nSUB\n'
    elif(val1 == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 1.0\nFSUB\n'

def p_operation_2plus(p):
    '''operation : 2PLUS'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '2+'\033[0m\n") 
    if(val1 == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 2\nADD\n'
    elif(val1 == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 2.0\nFADD\n'

def p_operation_2minus(p):
    '''operation : 2MINUS'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '2-'\033[0m\n") 
    if(val1 == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 2\nSUB\n'
    elif(val1 == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 2.0\nFSUB\n'

def p_operation_2times(p):
    '''operation : 2TIMES'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '2*'\033[0m\n") 
    
    if(val1 == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 2\nMUL\n'
    elif(val1 == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 2.0\nFMUL\n'

def p_operation_2divide(p):   
    '''operation : 2DIVIDE'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '2/'\033[0m\n") 
    
    if(val1 == "INT"):
        stack.append("INT")
        p[0] = f'PUSHI 2\nDIV\n'
    elif(val1 == "FLOAT"):
        stack.append("FLOAT")
        p[0] = f'PUSHF 2.0\nFDIV\n'

def p_operation_dup(p):
    '''operation : DUP'''
    try:
        val1 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'DUP'\033[0m\n")
    
    stack.append(val1)
    stack.append(val1)
    p[0] = f'DUP 1\n'
    
def p_operation_2dup(p):
    '''operation : 2DUP'''
    global regist_counter
    val1 = stack.pop()
    val2 = stack.pop()
    stack.append(val2)
    stack.append(val1)
    stack.append(val2)
    stack.append(val1)
    p[0] = f'STOREG {str(regist_counter + 1)}\nSTOREG {str(regist_counter)}\nPUSHG {str(regist_counter)}\nPUSHG {str(regist_counter+1)}\nPUSHG {str(regist_counter)}\nPUSHG {str(regist_counter+1)}\n'
    regist_counter += 2
    
def p_operation_drop(p):
    '''operation : DROP'''
    stack.pop()
    p[0] = f'POP 1\n'

def p_operation_swap(p):        
    '''operation : SWAP'''
    val1 = stack.pop()
    val2 = stack.pop()
    stack.append(val1)
    stack.append(val2)
    p[0] = f'SWAP\n'
    
def p_operation_depth(p):        
    '''operation : DEPTH'''
    stack_size = len(stack)
    p[0] = f'PUSHI {stack_size}\n'
        
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

#def p_line_definition(p):
#    '''line : COLON WORD CODE'''
 #   if p[2] in defined_words:
  #      p_err_2(p)
 #       raise Exception(f"\n\t\033[91m ERROR :: Word redefenition :: Word {p[2]} \033[0m\n")        
  #  else:
   #     defined_words[p[2]] = p[3]
    #    p[0] = ''

#def p_line_definition_error(p):
#    '''line : COLON WORD'''
#    p_err_2(p)
#    raise Exception(f"\n\t\033[91m ERROR :: No code in function defenition :: Check if missing function comment description\033[0m\n")        
    
#def p_line_word(p):
#    '''line : WORD'''
 #   if p[1] in defined_words:
  #      p[0] = p[1] + "\n"
  #  else:
  #      p_err_1(p)
   #     raise Exception(f"\n\t\033[91m ERROR :: Undefined Word :: \"{p[1]}\" \033[0m\n")        

def p_operation_plus(p):
    '''operation : PLUS'''
    
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'PLUS'\033[0m\n") 
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FADD\n'
    else:
        stack.append("INT")
        p[0] = f'ADD\n'
    

def p_operation_minus(p):
    '''operation : MINUS'''
    
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'MINUS'\033[0m\n") 
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FSUB\n'
    else:
        stack.append("INT")
        p[0] = f'SUB\n'

def p_operation_times(p):
    '''operation : TIMES'''
 
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'TIMES'\033[0m\n") 
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FMUL\n'
    else:
        stack.append("INT")
        p[0] = f'MUL\n'
    
def p_operation_divide(p):
    '''operation : DIVIDE'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'DIVIDE'\033[0m\n") 
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("FLOAT")
        p[0] = f'FDIV\n'
    else:
        stack.append("INT")
        p[0] = f'DIV\n'

def p_operation_mod(p):
    '''operation : MOD'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using 'MOD'\033[0m\n") 
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        print("Operacao impossivel com floats")
    else:
        stack.append("INT")
        p[0] = f'MOD\n'

def p_operation_sup(p):
    '''operation : SUP'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '>'\033[0m\n")
    
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("INT")
        p[0] = f'FSUP\n'
    else:
        stack.append("INT")
        p[0] = f'SUP\n'

def p_operation_equal(p):
    '''operation : EQUAL'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '=='\033[0m\n")
    
    stack.append("INT")
    p[0] = f'EQUAL\n'


def p_operation_inf(p):
    '''operation : INF'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '<'\033[0m\n")
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("INT")
        p[0] = f'FINF\n'
    else:
        stack.append("INT")
        p[0] = f'INF\n'

def p_operation_supequal(p):
    '''operation : SUPEQUAL'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '>='\033[0m\n")
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("INT")
        p[0] = f'FSUPEQ\n'
    else:
        stack.append("INT")
        p[0] = f'SUPEQ\n'

def p_operation_infequal(p):
    '''operation : INFEQUAL'''
    try:
        val1 = stack.pop()  
        val2 = stack.pop()
    except IndexError as e:
        p_err_1(p)
        raise Exception(f"\n\t\033[91m ERROR :: Stack Empty :: Using '<='\033[0m\n")
    if(val1 == "FLOAT" or val2 == "FLOAT" ):
        stack.append("INT")
        p[0] = f'FINFEQ\n'
    else:
        stack.append("INT")
        p[0] = f'INFEQ\n'
        
def p_empty(p):
    'empty :'
    pass
        
def p_error(p):
    if p:
        print("\nSyntax error at line", p.lineno, "column", find_column(data, p.lexpos))
    else:
        print("\nSyntax error: unexpected end of input")
        raise Exception(f"\n\t\033[91m FATAL :: Check last line for unwanted characters\033[0m\n")

def p_err_1(p):
    if p:
        print("\nSyntax error at line", p.lineno(1), "column", find_column(data, p.lexpos(1)))
    else:
        print("Syntax error: unexpected end of input")

def p_err_2(p):
    if p:
        print("\nSyntax error at line", p.lineno(2), "column", find_column(data, p.lexpos(2)))
    else:
        print("Syntax error: unexpected end of input")

def find_column(input, tokenLexpos):
    line_start = input.rfind('\n', 0, tokenLexpos) + 1
    return (tokenLexpos - line_start) + 1


vars = ''

def loop_vars():
    global regist_counter,vars
    for i in range(regist_counter):
        stack.append('INT')
        vars += 'PUSHI 0\n'
        
# Build the parser
parser = yacc.yacc()

# Test the parser
data=''': maior2 ( -- ) 2dup > if drop else swap drop then ;
    : maior3 ( -- ) maior2 maior2 ;
    : maiorN ( -- ) depth 1 do maior2 loop ;
    2 11 3 4 45 8 19 maiorN .
    '''

func_call_pattern = r':\s([a-zA-Z_][a-zA-Z0-9_]*)\s\([^)]*\)\s([^;]+)\s;'

matches = []
for match in re.finditer(func_call_pattern, data):
    func_name = match.group(1).strip() 
    func_content = match.group(2).strip()  
    defined_words[func_name] = func_content
    matches.append(match)

for match in reversed(matches):  # Iterate in reverse order to avoid changing indices
    start_index = match.start()
    end_index = match.end()
    data = data[:start_index] + data[end_index:]
    
replaced = True  
while replaced:
    replaced = False  
    for func_name, func_content in defined_words.items():
        
        func_call_pattern = re.compile(r'\b' + func_name + r'\b')
        data, count = re.subn(func_call_pattern, func_content, data)

        if count > 0:
            replaced = True 

print(defined_words)
print(data)

try:
    r = parser.parse(data)
except Exception as e:
    print(e)
    sys.exit()

loop_vars()
result = vars
result += "\nSTART\n\n"
result += r
result += "\nSTOP\n"

# Print the generated assembly code            
print(result)
