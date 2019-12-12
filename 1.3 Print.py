my_name = 'Dr. Anuprita Deshmukh'
my_age = 50 # not a lie
my_height = 152 # c.m.
my_weight = 70 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print ("%s, Let's talk about ." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy. " % my_weight)
print ("Actually that's not too heavy. ")
print ("He's got %s eyes and %s hair. " % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee. " % my_teeth)

# this line is tricky, try to get it exactly right
#print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight,( my_age + my_height + my_weight)))
