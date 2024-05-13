import ply.lex as lex
import sys
# List of token names
defined_words = {}

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
    'SPACE',
    'SPACES',
    'EMIT',
    'CHAR',
    'PONTOSTRING',
    '2DUP',
    'DUP',
    'DROP',
    'SWAP',
    'DEPTH',
    'COMMENT',
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
    '2DIVIDE',
)
# Regular expression rules for simple tokens

def t_PLUS(t):
    r'\+'
    return t
    
def t_MINUS(t):
    r'-'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'/'
    return t
    
def t_MOD(t):
    r'%'
    return t
    
def t_PONTOSTRING(t):
    r'."([^"]*)"'
    return t
    
def t_PONTO(t):
    r'\.'
    return t
    
def t_1PLUS(t):  
    r'1\+'
    return t

def t_1MINUS(t):  
    r'1-'
    return t
    
def t_2PLUS(t):  
    r'2\+'
    return t

def t_2MINUS(t):  
    r'2-'
    return t
    
def t_2TIMES(t):  
    r'2\*'
    return t
    
def t_2DIVIDE(t):  
    r'2/'
    return t

def t_EMIT(t):
  r'\bEMIT\b|\bemit\b'
  return t

def t_CHAR(t):
  r'\b(?:CHAR|char)\b\s.'
  return t

def t_CR(t):
    r'\bCR\b|\bcr\b'
    return t

def t_SPACE(t):
    r'\bSPACE\b|\bspace\b'
    return t

def t_SPACES(t):
    r'\bSPACES\b|\bspaces\b'
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

def t_2DUP(t):   
    r'\b2DUP\b|\b2dup\b'
    return t

def t_DROP(t):  
    r'\bDROP\b|\bdrop\b'
    return t
def t_SWAP(t):  
    r'\bSWAP\b|\bswap\b'
    return t
def t_DEPTH(t):  
    r'\bDEPTH\b|\bdepth\b'
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
 


