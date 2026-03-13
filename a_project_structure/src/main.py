from a_project_structure.src.module1 import thingy1
from a_project_structure.src.module2 import thingy2
import sys

args = sys.argv[:]
for arg in args:
    print(f"Found arg: {arg}")
return_value_module1 = thingy1.methode1()
return_value_module2 = thingy2.methode2()
print(f"Return 1 is {return_value_module1} return 2 is {return_value_module2}")
