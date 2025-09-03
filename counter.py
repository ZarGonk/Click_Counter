from random import randint

# Private state of the counter
_count = 0

def increment():
    """Increment the counter and return the new value."""
    global _count
    _count += 1
    return _count

def decrement():
    """Decrement the counter and return the new value."""
    global _count
    _count -= 1
    return _count

def reset():
    """Reset the counter to zero and return it."""
    global _count
    _count = 0
    return _count

def set_value(start):
    """Set an initial value for the counter and return it."""
    global _count
    _count = start
    return _count
    
def get_value():
    """Return the current value of the counter without modifying it."""
    return _count

def color_hex_random():
    """Generate and return a random HEX color string."""
    return '#{:06x}'.format(randint(0, 0xFFFFFF))