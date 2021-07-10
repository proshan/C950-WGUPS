from read_csv import *

# getting needed data structures for package, distance and address
package_hash = import_package_data()
distance_array = import_distance_data()
address_dict = import_address_data()

distance_travelled_list = []

# this function chooses the next stop according to the current stop provided in the particular truck
# with the implementation of nearest neighbor algorithm
def get_next_stop(current_stop, truck_number):
    # initializing nearest_stop distance to compare later on
    nearest_stop_distance = 30
    next_package_id = None
    next_address = None
    for p_id in truck_number:
        pa = package_hash.get_value(p_id)
        package_address_number = address_dict[pa.address][0]
        if package_address_number > current_stop:
            distance = float(distance_array[package_address_number][current_stop])
        else:
            distance = float(distance_array[current_stop][package_address_number])
        # checking if it is shor compared to others
        if distance < nearest_stop_distance:
            nearest_stop_distance = distance
            next_package_id = pa
            next_address = package_address_number
    return next_package_id, next_address, nearest_stop_distance

# this function will actually be the last function
# where the trucks will deliver the packages and the total distance traveled will be found
def run_truck(truck_number, start_time):
    # changing the package status to en route
    for package in truck_number:
        p = package_hash.get_value(package)
        p.status = "en route"
    starting_stop = 0
    # this total distance will only be for that particular truck
    total_distance = 0
    for item in range(len(truck_number)):
        p, starting_stop, distance = get_next_stop(starting_stop, truck_number)
        # the speed of truck is 18mph
        # start_time is in minutes
        start_time += int((distance/18) * 60)
        p.delivery_time = "{:02d}".format(int(start_time/60)) + ":" + "{:02d}".format(start_time % 60)
        # Updating delivery status
        p.delivery_status = "Package delivered at: " + p.delivery_time
        total_distance = distance + total_distance
        truck_number.remove(p.package_id)
    # time and distance to return to hub
    distance_to_reach_hub = float(distance_array[starting_stop][0])
    total_distance = total_distance + distance_to_reach_hub
    start_time = int((distance_to_reach_hub/18) * 60) + start_time
    return total_distance


def wgups_route():
    # manually loading the packages into the trucks
    truck_1 = [13, 14, 15, 16, 19, 20, 1, 37, 40, 21, 4, 26, 34, 29, 30]
    truck_2 = [3, 18, 36, 38, 6, 25, 28, 31, 32, 2]
    truck_3 = [5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39]

    # start time for truck 1 is 8AM (here, time is in minutes)
    truck1_start_time = 480
    # truck two is set to leave after the packages arrive at 9:06
    truck2_start_time = 546
    # truck three is set to leave after the truck1 finishes delivering and comes back at 10:20
    truck3_start_time = 620

    truck1_travelled_distance = run_truck(truck_1, truck1_start_time)
    truck2_travelled_distance = run_truck(truck_2, truck2_start_time)
    truck3_travelled_distance = run_truck(truck_3, truck3_start_time)

    distance_travelled_list.append(truck1_travelled_distance)
    distance_travelled_list.append(truck2_travelled_distance)
    # updating package number nine
    package_hash.get_value(9).notes = "Corrected address 10:20AM"
    distance_travelled_list.append(truck3_travelled_distance)

    distance_travelled_list.append((truck1_travelled_distance + truck2_travelled_distance + truck3_travelled_distance))





def display_ui():
    print("\n-----------Welcome to WGUPS-----------")
    print(".-. Enter \'wgups\' to get WGUPS delivery information.")
    print(".-. Enter time in a format HH:MM to get info of all packages at that time.")
    print(".-. Enter a package id to get that package information.")
    print(".-. Enter \'exit\' to exit the WGUPS application.\n")


if __name__ == '__main__':
    # calling the routing function
    wgups_route()
    # The routing program should run first in order to
    # get package and delivery information to set on variables
    # ---

    # initializing the user choice
    user_choice = " "
    # getting the options for the user to select
    while user_choice != "exit":
        display_ui()
        user_choice = input("Enter your choice: ")
        if user_choice.lower() == "wgups":
            print("Distance travelled by truck 1: " + str(distance_travelled_list[0]))
            print("Distance travelled by truck 2: " + str(distance_travelled_list[1]))
            print("Distance travelled by truck 3: " + str(distance_travelled_list[2]))
            # last item in this list is total distance travelled
            print("\n")
            print("Total Distance by all three trucks: " + str(distance_travelled_list[3]))
        elif ":" in user_choice:
            # creating delivered and not delivered package list
            delivered_package_list = []
            not_delivered_package_list = []
            for item in range(1, package_hash.get_hashtable_size()):
                package = package_hash.get_value(item)
                if package.delivery_time <= user_choice:
                    delivered_package_list.append(package)
                else:
                    not_delivered_package_list.append(package)
            # printing the packages from delivered list and not delivered list
            print("Delivered package list by : " + str(user_choice))
            for p in delivered_package_list:
                p.print_package_info()
            print("Packages not delivered by: " + str(user_choice))
            for p in not_delivered_package_list:
                p.print_package_info()
        elif len(user_choice) < 3:
                package_id = int(user_choice)
                if package_id in range(1, package_hash.get_hashtable_size() + 1):
                    package_hash.get_value(package_id).print_package_info()
                else:
                    print("Invalid package number!")
        else:
            if user_choice != "exit":
                print("Invalid choice!")


