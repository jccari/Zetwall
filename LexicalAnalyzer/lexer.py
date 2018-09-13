from colorama import init, Fore, Back, Style
import sys
import re


def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    #print (text, tag, pos)
                    tokens.append(token)
                break
        if not match:
            init(autoreset=True)
            sys.stderr.write(Fore.RED+'[ERROR] Illegal character: %s\n' % characters[pos])          
			#sys.exit(1)
            pos = pos + len(characters[pos])
        else:
        	pos = match.end(0)
    return tokens

def get_tokens(characters, token_expr):
	return lex(characters,token_expr)