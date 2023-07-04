"""
Default Regex Patterns for Using in Parameters
"""

all_patterns = [
    r'([a-zA-Z-0-9]{4,32})',  # mapbox - 1
    r'var(.*)=',  # find variable name starting with var
    r'const(.*)=',  # find variable name starting with const
    r'let(.*)=',  # find variable name starting with let
    r'var\s*([\w,]+)',
    r'const\s*([\w,]+)',
    r'let\s*([\w,]+)',
    r'class\s+(\w+)',  # class names
    r'(.*)\(\).*{',  # function names in a JS class
]
