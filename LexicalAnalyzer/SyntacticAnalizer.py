import sys
import re
from lexer import get_tokens  


token_exprs = [
	#(r'(void|float|int) \w*\([\w*,]*\w\)\{\n\}',	'FUNCTION'),
	(r'(void|int|char|float)', 'DATATYPE'),
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'=',                     'EQUAL'),
    (r'\(',                    'OPEN_PARENTHESIS'),
    (r'\)',                    'CLOSE_PARENTHESIS'),
    (r'\[',                    'OPEN_BRACKET'),
    (r'\]',                    'CLOSE_BRACKET'),
    (r'\{',                    'OPEN_KEY'),
    (r'\}',                    'CLOSE_KEY'),
    (r'\,',	    			   'COMA'),
    (r';',                     'SEMICOLON'),
    (r'\+',                    'PLUS'),
    (r'-',                     'MINUS'),
    (r'\*',                    'MULT'),
    (r'/',                     'DIVISION'),
    (r'<=',                    'LESS_THAN'),
    (r'<',                     'LESS'),
    (r'>=',                    'GREATHER_THAN'),
    (r'>',                     'GREATHER'),
    (r'=',                     'EQUAL'),
    (r'!=',                    'NOT_EQUAL'),
    (r'and',                   'AND'),
    (r'or',                    'OR'),
    (r'not',                   'NOT'),
    (r'if',                    'IF'),
    (r'then',                  'THEN'),
    (r'else',                  'ELSE'),
    (r'while',                 'WHILE'),
    (r'do',                    'DO'),
    (r'end',                   'END'),
    (r'return',				   'RETURN'),
    (r'[\d]+\.[\d]+',		   'FLOAT'),
	(r'[0-9]+',                'INT'),
	(r'\"[\w|\d]{1}\"',		   'CHAR'),
    (r'[A-Za-z][A-Za-z0-9_]*', 'IDENTIFIER')
]

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = get_tokens(characters,token_exprs)
    for token in tokens:
        print (token)
