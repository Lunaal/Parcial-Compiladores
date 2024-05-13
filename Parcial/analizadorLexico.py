import ply.lex as lex

tokens = (
    'print',
    'numeral',
    'float',
    'literal',
    'Boolean',
    'def',
    'oper_plus',
    'oper_min',
    'oper_mul',
    'oper_div',
    'left_p',
    'right_p',
    'Key_left',
    'Key_right',
    'Type_int',
    'Type_Boolean',
    'Type_float',
    'Type_String',
    'doper_equal',
    'oper_equal',
    'oper_diferent',
    'oper_moree',
    'oper_lesse',
    'oper_more',
    'oper_less', 
    'for',
    'while', 
    'identificador',
    'if',
    'else',
    'oper_com',
    'return',
    'oper_dotc',
  )

t_print = r'show'
t_oper_plus    = r'\+'
t_oper_min  = r'-'
t_oper_mul  = r'\*'
t_oper_div  = r'/'
t_left_p  = r'\('
t_right_p  = r'\)'
t_Key_left  = r'\{'
t_Key_right  = r'\}'
t_Type_int = r'int'
t_Type_Boolean = r'FiftyFifty'
t_Type_float = r'float'
t_oper_diferent = r'\!='
t_oper_moree     = r'\>=' 
t_oper_lesse    = r'\<='
t_oper_more    = r'\>' 
t_oper_less     = r'\<'
t_for  = r'repeat'
t_while  = r'meanwhile'
t_literal = r'\".*\"'
t_def = r'def'
t_if     = r'if'
t_else   = r'else'
t_oper_com = r'\,'
t_return = r'give'
t_oper_dotc  = r'\;'

def t_doper_equal(t):
  r'\=\='
  return t

def t_oper_equal(t):
  r'='
  return t

def t_identificador(t):
  r'([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|_)*'
  if (t.value == 'int'):
      t.type = 'Type_int'
      return t
  elif(t.value == 'FiftyFifty'):
      t.type = 'Type_Boolean'
  elif(t.value == 'true'):
      t.type = 'Boolean'
  elif(t.value == 'false'):
      t.type = 'Boolean'
  elif(t.value == 'float'):
      t.type = 'Type_Boolean'
  elif(t.value == 'String'):
      t.type = 'Type_string'
  elif(t.value == '(\".*\")|(“.*”)'):
      t.type = 'literal'
  elif(t.value == 'def'):
      t.type = 'def'
  elif(t.value == 'repeat'):
      t.type = 'for'
  elif(t.value == 'meanwhile'):
      t.type = 'while'
  elif(t.value == 'if'):
      t.type = 'if'
  elif(t.value == 'else'):
      t.type = 'else'
  elif(t.value == 'give'):
      t.type = 'return'
  elif(t.value == 'show'):
      t.type = 'print'
  
  return t

def t_float(t):
  r'\d+(\.\d+)'
  t.value = float(t.value)
  return t

def t_numeral(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def lector(filename):
  with open(filename,'r') as file:
    return file.read()


def test(data):
    lexer.input(data)
    output = []
    while True:
        tok = lexer.token()
        if not tok: 
            break 
        output.append(str(tok.type)) 
    entrada = " ".join(output)
    return entrada


filename = 'entrada.txt'
data = lector(filename)
tokens = test(data)

entrada = test(data)
print (entrada)