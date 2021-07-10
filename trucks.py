# manually loading the three wgu trucks based on following constraints:

# truck 1:
# package 14 must be delivered with package 15 and 19
# package 16 must be delivered with package 13 and 19
# package 20 must be delivered with package 13 and 15
def get_truck_one_packages():
    return [14, 15, 19, 16, 13, 20, 40, 17, 37, 30, 21, 26, 34, 4, 29]


# truck 2:
# package 3 can only be on truck 2
# package 6 has been delayed on flight (only arrives at 9:05)
# package 18, 36 and 38 can only be on truck two
# package 25, 28 and 32 only arrives at 9:05
def get_truck_two_packages():
    return [2, 3, 6, 18, 36, 38, 25, 28, 32, 31]


# truck 3:
# package 9 has wrong address listed
def get_truck_three_package():
    return [1, 5, 7, 8, 9, 10, 11, 12, 22, 23, 24, 27, 33, 35, 39]