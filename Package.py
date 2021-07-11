# Package class for WGUPS

from trucks import *
from read_csv import *


class Package:

    # here, package is a list containing id, address, city,zip, deadline, weight, notes,
    # delivery time and delivery status
    # initial delivery status for all package is "at hub"
    def __init__(self, package):
        self.package_id = int(package[0])
        self.address = package[1]
        self.city = package[2]
        self.state = package[3]
        self.zip = package[4]
        self.deadline = package[5]
        self.weight = package[6]
        self.notes = package[7]
        self.delivery_time = "00:00"
        self.delivery_status = "At hub"

    # this function is used to print the details of a particular package
    def print_package_info(self):
        print("Id: " + str(self.package_id) + " Address: " + str(self.address) + " City: " + str(self.city) +
              " State: " + str(self.state) + " Zip: " + str(self.state) + " Deadline: " + str(self.deadline) +
              " Weight: " + str(self.weight) + " Notes: " + str(self.notes) + " Time: "
              + str(self.delivery_time) + " Status: " + str(self.delivery_status))

    # create a function that takes in the user input time
    # compares it to delivered time
    # if the user input time is in between truck start time for package and delivered time, status = en route
    # if the user input time is less than truck start time, status = "in hub"
    # if the user input time is greater than or equal to delivered time, status = delivered
    # returns the package id
    def get_a_package_info(self, time):
        delivery_status = "in hub"
        truck_start_time = ""
        if self.get_package_id() in get_truck_one_packages():
            truck_start_time = "08:00"
        elif self.get_package_id() in get_truck_two_packages():
            truck_start_time = "09:06"
        elif self.get_package_id() in get_truck_three_package():
            truck_start_time = "10:20"
        if (time >= truck_start_time) and (time < self.delivery_time):
            delivery_status = "en route"
        elif time >= self.delivery_time:
            delivery_status = "delivered at " + self.delivery_time
        # printing with the delivery status detail
        print("Id: " + str(self.package_id) + " Address: " + str(self.address) + " City: " + str(self.city) +
              " State: " + str(self.state) + " Zip: " + str(self.state) + " Deadline: " + str(self.deadline) +
              " Weight: " + str(self.weight) + " Notes: " + str(self.notes)
              + " Status: " + " \"" + delivery_status + "\"")

    def get_package_id(self):
        return self.package_id

    # returns the package address
    def get_address(self):
        return self.address

    # returns the package city
    def get_city(self):
        return self.city

    # returns the package state
    def get_state(self):
        return self.state

    # returns the package zip
    def get_zip(self):
        return self.zip

    # returns the package deadline
    def get_deadline(self):
        return self.deadline

    # returns the package weight
    def get_weight(self):
        return self.weight

    # returns the package notes
    def get_notes(self):
        return self.notes

    # returns the package delivery time
    def get_delivery_time(self):
        return self.delivery_time

    # returns the package delivery status
    def get_delivery_status(self):
        return self.delivery_status

    # sets the value of notes to the package
    def set_notes(self, note):
        self.notes = note

    # sets the delivery status to the package
    def set_delivery_status(self, status):
        self.delivery_status = status







