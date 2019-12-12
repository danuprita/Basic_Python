formatter = "%r abc %r xyz %r pqr %r"
# The %r will give you the “raw programmer’s” version of variable, also known as the representation.
print (formatter % (1, 2, 3, 4))
print (formatter % ('one', "two", 'three', "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
))

# Python is going to print the strings in the most effi cient way it can,
# not replicate exactly the way you wrote them.