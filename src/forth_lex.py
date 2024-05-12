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
    'PONTOSTRING',
    'DUP',
    'DROP',
    'SWAP',
    'COMMENT',
    'COLON',   
    'SEMICOLON',  
    'WORD',
    'IF',
    'ELSE',
    'THEN',
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
t_COMMENT = r'\([^)]*\)'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
t_COLON   = r':'
t_SEMICOLON = r';'
t_1PLUS = r'1\+'
t_1MINUS = r'1-'
T_2PLUS = r'2\+'
t_2MINUS = r'2-'
t_2TIMES = r'2\*'
t_2DIVIDE = r'2/'

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

def t_CR(t):
    r'CR|cr'
    return t
def t_IF(t):    
    r'IF|if' 
    return t
def t_ELSE(t):  
    r'ELSE|else'
    return t
def t_THEN(t):  
    r'THEN|then'
    return t
def t_DUP(t):   
    r'DUP|dup'
    return t
def t_DROP(t):  
    r'DROP|drop'
    return t
def t_SWAP(t):  
    r'SWAP|swap'
    return t

def t_PONTOSTRING(t):
  r'."([^"]*)"'
  return t

# Regular expression for words
def t_WORD(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'  # Start with a letter or underscore, followed by letters, digits, hyphens, underscores, or dots
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
        