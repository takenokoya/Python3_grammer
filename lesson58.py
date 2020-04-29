import string
# template
s = """\
Hi $name.
$contents
Have a good day
"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents="How are ypu?")
print(contents)
