# Chaining HashTable Python
class Hash:
    # Constructor with optional initial capacity parameter
    def __init__(self, initial_len=10):
        self.main_table = []
        for i in range(initial_len):
            self.main_table.append([])

    # this will insert a key value pair in the hash bucket list.
    def insert_hash(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        current_bucket = hash(key) % len(self.main_table)
        bucket_list = self.main_table[current_bucket]
        for k_v in bucket_list:
            if k_v[0] == key:
                k_v[1] = item
                return True

        # if k_v is not in the bucket_list, it will get inserted to the end of the bucket_list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # This will search from hashtable
    # item will be returned if found, if not, None will be returned
    def search_hash(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.main_table)
        bucket_list = self.main_table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # removes an item from the bucket list with the provided key
    def remove_hash(self, key):
        current_bucket = hash(key) % len(self.main_table)
        bucket_list = self.main_table[current_bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
