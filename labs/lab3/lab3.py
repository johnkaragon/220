road = eval(input("How many roads were surveyed? "))
t_vehicles = 0
for i in range(0, road):
    message = "How many days was road " + str(i + 1) + " surveyed? "
    days = eval(input(message))
    t_cars = 0
    for j in range(0, days):
        message_2 = "How many cars passed through the road on day " + str(j+1) + "? "
        d_cars = eval(input(message_2))
        t_cars += d_cars
    t_vehicles += t_cars
    t_cars = t_cars / days
    print("Road ", (i+1), " average cars per day: ", t_cars)
print("Total cars on all roads: ", t_vehicles)
print("Total avg for all roads: ", (t_vehicles / road))
