"""
Module:
•	A module is a file consisting of python code
•	It can have functions, classes, variables
•	Any python file can be referred as a module

"""

"""
Types of modules:
User defined modules:
•	Created by user
•	Can be accessed using import keyword
"""

"example"
from practice_11_11_2023.functions.function_scopes import outer

"""import statement:
•	used to import modules in any program (if the file is in current working directory)
•	it can be written anywhere in the program
•	any number of modules imported in a module
•	Syntax: import module name
"""
"exapmle"
import new_file1

"""
From keyword:
•	It is used when we need to import some module from different package
•	Syntax: from module_name import function
o	from  package_name import module_name
o	from package_name.module_name import function
""""exapmle"
from itertools import zip_longest
from collections import defaultdict


"""
As keyword:
•	used to given an alias name for the module as well as function
•	Syntax: from module_name import function as alias_name
o	From package_name import module_name as alias name
o	From package_name.module_name import function as alias_name
"""

from collections import defaultdict as dd
dict_  = dd(int)
print(dict_)