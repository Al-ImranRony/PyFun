''' Using Python's built-in "dis" module to disassemble functions
    and inspect their CPython VM bytecode 
'''

import dis

def identity(name):
    return 'This is ' + name + ':/'

identity("Ron")

print(dis.dis(identity))