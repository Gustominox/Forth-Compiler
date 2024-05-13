import ply.lex as lex
import sys
# List of token names
tokens = (
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES', 
    'DIVIDE',
    'MOD',
    'PONTO',
    'CR',
    'EMIT',
    'CHAR',
    'PONTOSTRING',
    'DUP',
    'DROP',
    'SWAP',
    'COMMENT',
    'COLON',   
    'SEMICOLON',  
    'WORD',
    'CODE',
    # CONDICIONAIS
    'IF',
    'ELSE',
    'THEN',
    # CICLOS
    "DO",
    "LOOP",
    # OPERACOES CONDICIONAIS
    'SUP',
    'EQUAL',
    'INF',
    'SUPEQUAL',
    'INFEQUAL',
    # ATALHOS
    '1PLUS',
    '1MINUS',
    '2PLUS',
    '2MINUS',
    '2TIMES',
    '2DIVIDE'
)
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_PONTO   = r'\.'
t_1PLUS = r'1\+'
t_1MINUS = r'1-'
T_2PLUS = r'2\+'
t_2MINUS = r'2-'
t_2TIMES = r'2\*'
t_2DIVIDE = r'2/'

def t_EMIT(t):
  r'\bEMIT\b|\bemit\b'
  return t

def t_CHAR(t):
  r'\bCHAR\b|\bchar\b'
  return t

def t_COLON(t): 
    r':'
    return t

def t_CR(t):
    r'\bCR\b|\bcr\b'
    return t

def t_IF(t):    
    r'\bIF\b|\bif\b' 
    return t

def t_ELSE(t):  
    r'\bELSE\b|\belse\b'
    return t

def t_THEN(t):  
    r'\bTHEN\b|\bthen\b'
    return t
def t_DUP(t):   
    r'\bDUP\b|\bdup\b'
    return t
def t_DROP(t):  
    r'\bDROP\b|\bdrop\b'
    return t
def t_SWAP(t):  
    r'\bSWAP\b|\bswap\b'
    return t


def t_DO(t):
    r'\bDO\b|\bdo\b'
    return t

def t_LOOP(t):
    r'\bLOOP\b|\bloop\b'
    return t

def t_SUPEQUAL(t):
    r'>='
    return t

def t_INFEQUAL(t):
    r'<='
    return t

def t_SUP(t):
    r'>'
    return t

def t_EQUAL(t):
    r'='  
    return t

def t_INF(t):
    r'<'
    return t

def t_PONTOSTRING(t):
  r'."([^"]*)"'
  return t

# Regular expression for words
def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  # Start with a letter or underscore, followed by letters, digits, hyphens, underscores, or dots
    return t

def t_CODE(t):
    r'\([^)]*\) [^;]+ ;'
    return t

def t_SEMICOLON(t): 
    r';'
    return t


def t_COMMENT(t):
    r'\([^)]*\)'
    return t

# Regular expression for floats
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convert to float
    return t

# Regular expression for integers
def t_INT(t):
    r'\d+'
    t.value = int(t.value)  # Convert to integer
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule for illegal tokens
def t_error(t):
    print(f"Illegal token '{t.value}' at line {t.lineno}, position {find_column(t)}")
    raise Exception("Lexer stopped due to error")

# Function to find column position of token
def find_column(token):
    line_start = token.lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return token.lexpos - line_start + 1

# Build the lexer

lexer = lex.lex()

def debug_lexer(exemplo):
    lexer.input(exemplo)

    while tok := lexer.token():
        print(tok)
 
# Test the parser
#data='''
#: func1 ( -- ) if ."Sucesso1" CR else ."Falha1" CR then ;
#1 func1'''

#debug_lexer(data)