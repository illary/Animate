#--------------------------------------------------------------------------------------------------------------
# Contributors: Wilfredo Montanez, Martin Rivera, Jose Rodriguez, Illary Lopez
# Date: April, 1, 2016
# Team: Animate
# FP: Lexical Analyzer
#---------------------------------------------------------------------------------------------------------------

import ply.lex as lex


#Format for Animate {'<reserved_word>':'<token_name>'}
reserved = {
    'createframe':'CREATEFRAME',
    'rectangle': 'RECTANGLE',
    'circle': 'CIRCLE',
    'triangle': 'TRIANGLE',
    'animate': 'ANIMATE',
    'image': 'IMAGE'

}

#Token list

tokens = ['LPAREN','RPAREN','COM','NUMBER','ID'] + list(reserved.values())

# Regex rules for the tokens

t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_COM       = r'\,'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

# Regex para encontrar nombres de varialbles ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


