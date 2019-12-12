x = "There are %d types of people." % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary , do_not)
print (x)
print (y)
print ("I said: %r." % x)
print ("I also said: '%s'."% y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# The %r will give you the “raw programmer’s” version of variable, also known as the representation.
print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)


from datetime import date
today = date.today()
# yyyy-mm-dd
print("Today is great day, Since We started Learning Data Science From " , today)
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 = ", d1)
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 = ", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 = ", d3)
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 = ", d3)


