
## THE PROBLEM OF CHOOSING TRANSPORTATION 

## CONTEST

## user
user_departure_name = "Chisinau"
user_departure_km = 0
user_destination_name = "Balti"
user_destination_km = 120
user_roud_max_duration_h = 1

# transportaion option
# - wolking
transport_walk_speed_km_h = 10
# - bike
transport_bike_speed_km_h = 40
# - car
transport_car_speed_km_h = 120
# - bus
transport_bus_speed_km_h = 60

####### HELPER FUNCTIONS ##########
def calcDistance(u_dep, u_des):
    distance_km = abs(u_des - u_dep)
    return distance_km

def calcDuration (dist, t_speed):
    duration_h = dist / t_speed
#    print(dist, t_speed, duration_h)
    return duration_h

def evaluate_Transport (u_dep, u_des, u_max_dur, t_speed):
    distance_km = calcDistance(u_dep, u_des)
    duration_h  = calcDuration(distance_km, t_speed)
    answer      = duration_h <= u_max_dur 
    return answer

def printResolt():
        print("\nThe distanse between ", user_departure_name, "and", user_destination_name, "is", distance_km, "km" )
    
    

#####@@ DECISION MAKING #######

# --------------- CAR -----------------
answer_a = evaluate_Transport(user_departure_km, user_destination_km, user_roud_max_duration_h, transport_car_speed_km_h)
distance_km = calcDistance(user_departure_km, user_destination_km)
duration_h = calcDuration(distance_km, transport_car_speed_km_h)
printResolt()


#print("\nThe distanse between ", user_departure_name, "and", user_destination_name, "is", distance_km, "km" )
print("The estimated duration with CAR is  = ", duration_h, "h")
# --------------- CAR -----------------


# ---------------- BUS -------------------------
answer_b = evaluate_Transport(user_departure_km, user_destination_km, user_roud_max_duration_h, transport_bus_speed_km_h)
distance_km = calcDistance(user_departure_km, user_destination_km)
duration_h = calcDuration(distance_km, transport_bus_speed_km_h)
# print("\nThe distanse between ", user_departure_name, "and", user_destination_name, "is", distance_km, "km" )
print("The estimated duration with BUS is  = ", duration_h, "h")
# --------------- BUS -------------------------

# --------------- BIKE -----------------
answer_c = evaluate_Transport(user_departure_km, user_destination_km, user_roud_max_duration_h, transport_bike_speed_km_h)
distance_km = calcDistance(user_departure_km, user_destination_km)
duration_h = calcDuration(distance_km, transport_bike_speed_km_h)
# print("\nThe distanse between ", user_departure_name, "and", user_destination_name, "is", distance_km, "km" )
print("The estimated duration with BIKE is = ", duration_h, "h")
# --------------- BIKE -----------------

# --------------- WOLK -----------------
answer_w = evaluate_Transport(user_departure_km, user_destination_km, user_roud_max_duration_h, transport_walk_speed_km_h)
distance_km = calcDistance(user_departure_km, user_destination_km)
duration_h = calcDuration(distance_km, transport_walk_speed_km_h)

#print("\nThe distanse between ", user_departure_name, "and", user_destination_name, "is", distance_km, "km" )
print("The estimated duration WALKING is   = ", duration_h, "h")
# --------------- WOLK -----------------

if answer_a == True:
    print("CAR is ok ")
else:
    print("CAR is NOT ok ")
if answer_b == True:
    print("Bus is ok ")
else:
    print("BUS is NOT ok ")

if answer_c == True:
    print("BIKE is ok ")
else :
    print("BIKE is NOT ok ")

if answer_w == True:
    print("WALK is ok ")
else:
    print("WALK is NOT ok ")


# -----------CHOISING ONLY ONE SOLUTION ---------------#
print("\nFor the case to choise ONLY ONE SOLUTION")
if answer_a == True:
    print("CAR is ok ")
elif answer_b == True:
    print("Bus is ok ")
elif answer_c == True:
    print("BIKE is ok ")
elif answer_w == True:
    print("WALK is ok ")
else:
    print("No solution ! ")
# -----------CHOISING ONLY ONE SOLUTION ---------------#





# conditions
# if / if - else 
# functions


###### IF ELSE | CONCCURENT | INDEPENDENT 
#
#
#
#



