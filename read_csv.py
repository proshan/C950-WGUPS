# this class imports all the data from wgu_address_data.csv, wgu_distance_data.csv and wgu_package_data.csv
import csv
# importing Package class
from Package import Package

# importing chaining has table
from HashTable import Hash

# getting the filename in respective variables
package_filename = "wgu_package_data.csv"
distance_filename = "wgu_distance_data.csv"
address_filename = "wgu_address_data.csv"

# creating new instance of Hash Class
hash_table = Hash()


# reading distance from the table
# the distance will be stored in two dimensional array (matrix)
# -> O(n)
def import_distance_data():
    with open(distance_filename, 'r', encoding="utf-8-sig") as file:
        distance_list = []
        file_reader = csv.reader(file)
        for line in file_reader:
            distance_list.append(line)
        return distance_list


# this function imports the package information from 'wgu_package_data.csv'
# and stores in the hash table with key=<package_id> and value=<package_information>
# -> O(n)
def import_package_data():
    with open(package_filename, 'r', encoding="utf-8-sig") as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            package = Package(line)
            hash_table.insert_hash(package.package_id, package)
        return hash_table


# this function imports the addresses from the wgu_address_data.csv
# and stores the address as key and
# a list of address id and address name as value in a dictionary
# -> O(n)
def import_address_data():
    with open(address_filename, 'r', encoding="utf-8-sig") as file:
        file_reader = csv.reader(file)
        address_dictionary = {}
        for line in file_reader:
            address_dictionary[line[0]] = [int(line[1]), line[2]]
        return address_dictionary







