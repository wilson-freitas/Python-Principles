def validate(code_str):

    if 'def' not in code_str:
        return "missing def"
    
    elif ':' not in code_str:
        return "missing :"
    
    elif '(' not in code_str or ')' not in code_str:
        return "missing paren"
    
    elif code_str.index(')') - code_str.index('(') == 1:
        return "missing param"
    
    elif "    " not in code_str:
        return "missing indent"
    
    elif "validate" not in code_str:
        return "wrong name"
    
    elif "return" not in code_str:
        return "missing return"
    
    else:
        return True