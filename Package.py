# Package class for WGUPS

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

    def print_package_info(self):
        print("Package Id: " + str(self.package_id) + " Address: " + str(self.address) + " City: " + str(self.city) +
              " State: " + str(self.state) + " Zip: " + str(self.state) + " Deadline: " + str(self.deadline) +
              " Weight: " + str(self.weight) + " Notes: " + str(self.notes) + " Delivery Time: "
              + str(self.delivery_time) + " Status: " + str(self.delivery_status))








