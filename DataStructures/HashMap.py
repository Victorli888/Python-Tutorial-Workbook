# Hash Map Class that uses Linear Open Addressing to solve Hash Collisions
class HashMap:

    def __init__(self, array_size):
        """
        Python does not have a static array by default, so to simulate how lower languages would handle Hash Maps. for the array size create a null item at each index
        :param array_size: positive integer that determines the number of null items in our array.
        """
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        """
    Take our key & create a hash code
    :param key: String operand that will be hashed by the method
    :param count_collisions: When Hash Collision occurs increment by 1 and create a new hash
    :return: the sum after UTF-8 Encode plus the number of collisions that occurred, if any.
    """
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        '''
    Take our hash code and modulo by the array's total size to determine which index of the array it will be stored at
    :param hash_code: The result from after hashing our key with the hash() method
    :return: The array intended array index
        '''
        return hash_code % self.array_size

    def assign(self, key, value):

        """
        When the key value pair is given check if our key will provide an index in our array to store the value. If a collision occurs use open adressing to find a new index to store our value
        """
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision!

        number_collisions = 1

        while (current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        """
        From the key find the index where its value should be stored in the array, If a Retrieval Collision occurs use Open Adressing to find a new value
        """

        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


hash_map = HashMap(15)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
