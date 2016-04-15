# Yacc example

import ply.yacc as yacc
import time
import WindowsCreater
#Avaiable colors 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta'
colors=["white","black","red","green","blue","cyan","yellow","magenta"]
# Get the token map from the lexer.  This is required.
from Animate_Lex import tokens

def p_init_frame(p):
    'expression : CREATEFRAME LPAREN NUMBER COM NUMBER RPAREN'
    WindowsCreater.createNewCanvas(int(p[3]),int(p[5]))

    p[0]="Frame Created"


def p_create_rectangle(p):
    'expression : ID RECTANGLE LPAREN NUMBER COM NUMBER COM NUMBER COM NUMBER RPAREN'
    if colors.count(p[1])==0:
        print("Color is not avaiable, setting color to white")
        p[1]="white"
    WindowsCreater.createRectangle(int(p[4]),int(p[6]),int(p[8]),int(p[10]),p[1])

    p[0]="Rectangle Created"

def p_create_triangle(p):
    'expression : ID TRIANGLE LPAREN NUMBER COM NUMBER COM NUMBER COM NUMBER COM NUMBER COM NUMBER RPAREN'
    WindowsCreater.createTriangle(int(p[4]),int(p[6]),int(p[8]),int(p[10]),int(p[12]),int(p[14]),p[1])
    if colors.count(p[1])==0:
        print("Color is not available, setting color to white")
        p[1]="white"

    p[0]="Triangle Created"


def p_create_circle(p):
    'expression : ID CIRCLE LPAREN NUMBER COM NUMBER COM NUMBER RPAREN'
    WindowsCreater.createCircle(int(p[4]),int(p[6]),int(p[8]),p[1])
    if colors.count(p[1])==0:
        print("Color is not avaiable, setting color to white")
        p[1]="white"

    p[0]="Circle Created"

def p_image(p):
    'expression : IMAGE LPAREN ID COM NUMBER COM NUMBER RPAREN'
    WindowsCreater.loadimage(p[3],int(p[5]),int(p[7]))
    p[0]="Image Inserted Created"

def p_animate(p):
    'expression : ANIMATE LPAREN NUMBER COM NUMBER COM NUMBER COM NUMBER RPAREN'
    WindowsCreater.run(int(p[3]),int(p[5]),int(p[7]), int(p[9]))
    p[0]="Starting Animation"


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('Animate > ')
       s.lower()
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
