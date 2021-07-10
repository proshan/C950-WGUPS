import csv
# importing Package class
from Package import Package

# importing chaining has table
from HashTable import Hash

# getting the filename in respective variables
package_filename = "package.csv"
distance_filename = "distance.csv"
address_filename = "address.csv"

# creating new instance of Hash Class
hash_table = Hash()

# reading distance from the table
# the distance will be stored in two dimensional array (matrix)
def import_distance_data():
    with open(distance_filename, 'r', encoding="utf-8-sig") as infile:
        distance_list = []
        file_reader = csv.reader(infile)
        for row in file_reader:
            distance_list.append(row)
        return distance_list


# this function imports the package information from 'package.csv'
# and stores in the hash table with key=<package_id> and value=<package_information>
def import_package_data():
    with open(package_filename, 'r', encoding="utf-8-sig") as infile:
        file_reader = csv.reader(infile)
        for row in file_reader:
            package = Package(row)
            hash_table.insert_hash(package.package_id, package)
        return hash_table

# this function imports the addresses from the address.csv
# and stores the address as key and
# a list of address id and address name as value in a dictionary
def import_address_data():
    with open(address_filename, 'r', encoding="utf-8-sig") as infile:
        file_reader = csv.reader(infile)
        address_dictionary = {}
        for row in file_reader:
            address_dictionary[row[0]] = [int(row[1]), row[2]]
        return address_dictionary







