import ply.lex as lex

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
    'DUP',
    'DROP',
    'SWAP',
    'OVER',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_PONTO   = r'\.'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_DUP     = r'DUP'
t_DROP    = r'DROP'
t_SWAP    = r'SWAP'
t_OVER    = r'OVER'

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

# Test the lexer
# data = '''30.5 5 - .'''
# Give the lexer some input

# lexer.input(data)

# Print tokens
# for token in lexer:
#     print(token)
