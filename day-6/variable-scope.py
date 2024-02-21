# Local - inside func
# Enclosing - exist only in nested functions
# Global - variables defined on top scr lvl (inside a module)
# Build-in - src env

name = 'Ula global'
def disp_loc():
    name = 'Ula func'
    print(name)

def disp_glob():
    print(name)


disp_loc()
disp_glob()
print(name)

