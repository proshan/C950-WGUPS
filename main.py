# Roshan Parajuli
# Student Id: 001476964

from read_csv import *
from trucks import *

# getting needed data structures for package, distance and address
# these import functions coming from read_csv
package_hash = import_package_data()
distance_array = import_distance_data()
address_dict = import_address_data()

# creating a lis to hold four items
# first - distance travelled by truck 1
# second - distance travelled by truck 2
# third - distance travelled by truck 3
# fourth - total distance travelled by all three trucks
distance_travelled_list = []


# function to display list of options to the user (UI)
def display_ui():
    print("\n-----------Welcome to WGUPS-----------")
    print(".-. Enter \'wgups\' to get WGUPS delivery information.")
    print(".-. Enter time in a format HH:MM to get info of all packages at that time.")
    print(".-. Enter a package id to get that package information.")
    print(".-. Enter \'exit\' to exit the WGUPS application.\n")


# this function chooses the next stop according to the current stop provided in the particular truck
# with the implementation of Nearest Neighbor Algorithm with complexity O(n)
def get_next_stop(current_stop, truck_number):
    # initializing nearest_stop distance to compare later on
    nearest_stop_distance = 30
    next_package_id = None
    next_address = None
    for p_id in truck_number:
        pa = package_hash.get_value(p_id)
        package_address_number = address_dict[pa.address][0]
        if package_address_number < current_stop:
            distance = float(distance_array[current_stop][package_address_number])
        else:
            distance = float(distance_array[package_address_number][current_stop])
        # checking if it is short compared to others
        # and updating the values to the nearest package destination
        if distance < nearest_stop_distance:
            nearest_stop_distance = distance
            next_package_id = pa
            next_address = package_address_number
    return next_package_id, next_address, nearest_stop_distance


# takes the distance traveled (in miles) and returns the number of minutes need to cover it
# -> O(1)
def get_time_spent(dist):
    return int((dist/18) * 60)


# this function will actually be the last function
# where the trucks will deliver the packages and the total distance traveled will be found
# get_next_stop() function is called so Complexity is O(n^2)
def run_truck(truck_number, start_time):
    # changing the package status to en route
    for package in truck_number:
        p = package_hash.get_value(package)
        status_string = "en route"
        p.set_delivery_status(status_string)
    starting_stop = 0
    # this total distance will only be for that particular truck
    total_distance = 0
    for item in range(len(truck_number)):
        p, starting_stop, distance = get_next_stop(starting_stop, truck_number)
        # the speed of truck is 18mph
        # start_time is in minutes
        start_time = get_time_spent(distance) + start_time
        p.delivery_time = "{:02d}".format(int(start_time/60)) + ":" + "{:02d}".format(start_time % 60)
        # Updating delivery status
        p.set_delivery_status("Package delivered at: " + p.delivery_time)
        total_distance = distance + total_distance
        truck_number.remove(p.get_package_id())
    # time and distance to return to hub
    distance_to_reach_hub = float(distance_array[starting_stop][0])
    total_distance = total_distance + distance_to_reach_hub
    start_time = get_time_spent(distance_to_reach_hub) + start_time
    return total_distance


# this function runs all the three wgu trucks to deliver packages
# and collects total distance travelled by each trucks and all trucks storing it in distance_travelled_list[]
# Complexity is O(n^2) from run_truck() function
def wgups_route():
    # pulling the manually loaded packages in the truck
    truck_1 = get_truck_one_packages()
    truck_2 = get_truck_two_packages()
    truck_3 = get_truck_three_package()

    # start time for truck 1 is 8AM (here, time is in minutes)
    truck1_start_time = 480
    # truck two is set to leave after the packages arrive at 9:06
    truck2_start_time = 546
    # truck three is set to leave after the truck1 finishes delivering and comes back at 10:20
    truck3_start_time = 620

    # sending the trucks for package delivery
    # we'll get the traveled distance by each trucks
    truck1_travelled_distance = run_truck(truck_1, truck1_start_time)
    truck2_travelled_distance = run_truck(truck_2, truck2_start_time)
    truck3_travelled_distance = run_truck(truck_3, truck3_start_time)

    distance_travelled_list.append(truck1_travelled_distance)
    distance_travelled_list.append(truck2_travelled_distance)
    # updating package number nine
    updated_note_for_9 = "Corrected address 10:20AM"
    package_hash.get_value(9).set_notes(updated_note_for_9)
    distance_travelled_list.append(truck3_travelled_distance)
    distance_travelled_list.append((truck1_travelled_distance + truck2_travelled_distance + truck3_travelled_distance))


# this function displays the distances travelled by each trucks
# and also the total distance covered by all the trucks to deliver all the packages
# -> O(1)
def print_travelled_distances():
    print("Distance travelled by truck 1: " + "{:.2f}".format(distance_travelled_list[0]))
    print("Distance travelled by truck 2: " + "{:.2f}".format(distance_travelled_list[1]))
    print("Distance travelled by truck 3: " + "{:.2f}".format(distance_travelled_list[2]))
    # last item in this list is total distance travelled
    # rounding up to two decimal places for the total distance travelled
    print("\nTotal Distance by all three trucks: " + "{:.2f}".format(distance_travelled_list[3]))


# this function takes the user input from UI and displays the information on packages in the provided time
# also displays the delivery status of the packages at given time
# -> O(1)
def package_details_at_particular_time(user_input):
    for item in range(1, package_hash.get_hashtable_size() + 1):
        package = package_hash.get_value(item)
        package.get_a_package_info(user_input)


# this function takes in the package_id as integer and provides the information on that particular package
# -> O(1)
def handle_single_package_information(user_selection):
    package_id = int(user_selection)
    # finding the package whose id is the user_choice's value
    if package_id in range(1, package_hash.get_hashtable_size() + 1):
        # printing the package details
        package_hash.get_value(package_id).print_package_info()
    else:
        print("Invalid package number!")


# main program start
if __name__ == '__main__':
    # calling the routing function
    wgups_route()
    # The routing program should run first in order to
    # get package and delivery information to set on the variables

    # initializing the user choice
    user_choice = " "
    # getting the options for the user to select
    while user_choice != "exit":
        display_ui()
        user_choice = input("$input->  ")
        if user_choice.lower() == "wgups":
            print_travelled_distances()
        elif ":" in user_choice:
            # checking if the entered time is in format of HH:MM (total length of 5)
            if len(user_choice) < 5:
                print("Time not in correct format!")
            else:
                package_details_at_particular_time(user_choice)
        # if the entered data's length is less than 3, it should be the id of the package that user entered
        elif len(user_choice) < 3:
            handle_single_package_information(user_choice)
        else:
            if user_choice != "exit":
                print("Invalid choice!")


