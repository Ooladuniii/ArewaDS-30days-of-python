# Approach 1: import module name
from my_function import greet

greet("Alice")

# Approach 2: from module name import function name
from my_function import greet

greet("Bob")

# Approach 3: import module name as alias
import my_function as mf

mf.greet("Charlie")

# Approach 4: from module name import function name as alias
from my_function import greet as gr

gr("David")
