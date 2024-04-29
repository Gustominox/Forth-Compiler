#
# (1)
# (aahah)
# (True,false)
# (1,aa, 2, bbb, TRUE, 3,False)
#

import sys
import ply.yacc as yacc
from listas_mistas_lex import tokens

def p_list(p):
    "LIST : LPAREN ELS RPAREN"
    p[0] = p[2]
    if (parser.cntN != parser.cntP):
        print("Erro Semantico: O número de PALAVRAS e INTEIROS é Diferente!")

def p_els_varios(p):
    "ELS : ELS VIRG EL"
    parser.conta += 1
    p[0] = p[1]
    if (p[3] != []):
       p[0].append(p[3])

def p_els_um(p):
    "ELS : EL"
    parser.conta = 1
    if (p[1]):
        p[0] = [p[1]]
    else:
        p[0] = []

def p_el_num(p):
    "EL : NUM"
    parser.soma += p[1]
    parser.cntN += 1
    p[0] = []

def p_el_bool(p):
    "EL : BOOL"
    p[0] = p[1]

def p_el_id(p):
    "EL : ID"
    parser.pals.append(p[1])
    parser.cntP += 1
    p[0] = []

def p_error(p):
    print("Syntax error!")
    parser.sucesso = False

parser = yacc.yacc()

for linha in sys.stdin:
    parser.sucesso = True
    parser.conta = 0
    parser.cntP = 0
    parser.cntN = 0
    parser.soma = 0
    parser.pals = []
    out = parser.parse(linha)
    if parser.sucesso:
       print("Lista sintetizada de Booleanos: ",out)
       print ("Informação final relativa ao processamento da frase analisada:")
       print("O total de elementos é : ", parser.conta)
       print("A soma é : ", parser.soma)
       print("As palavras são : ", parser.pals)


#parser.conta = 0
#parser.cntP = 0
#parser.cntN = 0
#parser.soma = 0
#parser.pals = []
#arser.sucesso = True
#fonte = ""
#for linha in sys.stdin:
    #fonte += linha
#parser.parse(fonte)
#if parser.sucesso:
#    print ("Parsing teminou com sucesso!")
#    print ("Informação final relativa ao processamento da frase analisada:")
#    print("O total de elementos é : ", parser.conta)
#    print("A soma é : ", parser.soma)
#    print("As palavras são : ", parser.pals)
