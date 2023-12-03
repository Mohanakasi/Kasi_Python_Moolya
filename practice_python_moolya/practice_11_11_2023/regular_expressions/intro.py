"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

"""
"""to regular expression operations we need to impoort module called re"""
"""in regular expression we will use some character and special seqquences for matching pattern"""
" meta characters & special sequences"
"""
meta characters
[]  set of characters
\   special sequence
. Any character (except new line)
*   zero or more
+  one or more
?  zero or one
{}  exactly specified no of occurances
|   either
()  capture  and group
"""

#
# \A  matchs the pattern at the beginning of the string
# \b  matches the pattern at the beginning or end of the string
# \B  matches at any where in the string
# \d matches the digits from 0-9
# \D  matches all other than digits
# \s matches white spaces
# \S matches all other than white spaces
# \w matches all word characters (a-z, A-Z, 0-9)
# \W matches other than word characters
# \Z matches charactes at the end of the string

"""methods in re
findall() --> returns a list containing all matched objects
serach()  --> returns a match object if there is a match anywhere in the string 
split()   --> Returns a list where the string has been split at each match
sub()     --> replaces one or many matches with a string"""

