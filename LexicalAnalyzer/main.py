import re

text = 'int function(a,b,c){\n}'

regex = re.compile(r'(void|float|int) \w*\([\w*,]*\w\)\{\n\}')
match = regex.match(text, 0)

if match:
	print (match.group(0))
else :
	print ("not match")

#exp = re.findall(r'(int|char) [\w]+', text)
#print (exp)

'''
token_exprs = [
	#(r'(void|float|int) \w*\([\w*,]*\w\)\{\n\}',	'FUNCTION'),
	(r'(void|int|char|float)', 'DATATYPE'),
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'=',                     RESERVED),
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r'\,',	    			   'COMA'),
    (r';',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'=',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'and',                   RESERVED),
    (r'or',                    RESERVED),
    (r'not',                   RESERVED),
    (r'if',                    RESERVED),
    (r'then',                  RESERVED),
    (r'else',                  RESERVED),
    (r'while',                 RESERVED),
    (r'do',                    RESERVED),
    (r'end',                   RESERVED),
    (r'return',				   RESERVED),
    (r'[\d]+\.[\d]+',		   FLOAT),
	(r'[0-9]+',                INT),
	(r'\"[\w|\d]{1}\"',		   CHAR),
    (r'[A-Za-z][A-Za-z0-9_]*', ID)
]
'''