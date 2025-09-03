from random import randint

# Estado privado do contador
_count = 0

def increment():
    """Incrementa o contador e retorna o novo valor."""
    global _count
    _count +=1
    return _count

def decrement():
    """Decrementa o contador e retorna o novo valor."""
    global _count
    _count -= 1  
    return _count


def reset():
    """Reseta o contador para zero e retorna o valor."""
    global _count 
    _count = 0
    return _count

def set_value(start):
    """Define um valor inicial para o contador e retorna-o."""
    global _count
    _count = start
    return _count
    
def get_value():
    """Retorna o valor atual do contador sem modificá-lo."""
    return _count

def color_hex_random():
    return '#{:06x}'.format(randint(0, 0xFFFFFF))