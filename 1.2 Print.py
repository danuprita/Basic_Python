cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are "+ str(cars)+ " cars available.")
print ("There are only "+ str(drivers)+" drivers available.")
print ("There will be "+ str(cars_not_driven)+ " empty cars today.")
print ("We can transport  "+ str(carpool_capacity)+ "  people today.")
print ("We have"+passengers+"to carpool today.")
print ("We need to put about"+ average_passengers_per_car+ "in each car.")


print ("There are %d " % cars + "cars available.")
print ("There are only %d " % drivers + " drivers available.")
print ("There will be %d " % cars_not_driven+ " empty cars today.")
print ("We can transport %d " % carpool_capacity+ " people today.")
print ("We have %d " % passengers+ " to carpool today.")
print ("We need to put about %d " % average_passengers_per_car+ " in each car.")
print ("We need to put about %d " % average_passengers_per_car, " in each car.")

print ("There are %d " %  cars + "cars available.")
