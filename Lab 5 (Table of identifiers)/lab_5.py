import random

# Function to calculate the projection hash value for an identifier
def projection_hash(identifier, table_size):
    """Calculate the projection hash value for an identifier."""
    hash_value = 0
    for char in identifier:
        hash_value += ord(char) # add the ASCII value of each character
    return hash_value % table_size # return the hash value modulo table size

# Class representing a hash table using projection hashing
class ProjectionHashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)] # create a list of empty lists

    def insert(self, identifier):
        """Insert an identifier into the hash table."""
        hash_value = projection_hash(identifier, self.table_size)
        self.table[hash_value].append(identifier)

    def search(self, identifier):
        """Search for an identifier in the hash table."""
        hash_value = projection_hash(identifier, self.table_size)
        if identifier in self.table[hash_value]:
            return True
        return False

# Class representing an ordered list
class OrderedList:
    def __init__(self):
        self.list = []

    def insert(self, identifier):
        """Insert an identifier into the ordered list."""
        # Find the correct position for the identifier in the list
        index = 0
        while index < len(self.list) and self.list[index] < identifier:
            index += 1
        self.list.insert(index, identifier)

    def search(self, identifier):
        """Search for an identifier in the ordered list."""
        # Use binary search to find the identifier in the list
        low = 0
        high = len(self.list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.list[mid] == identifier:
                return True
            elif self.list[mid] < identifier:
                low = mid + 1
            else:
                high = mid - 1
        return False

# Read the list of identifiers from a text file
with open('identifiers.txt', 'r') as file:
    identifiers = [line.strip() for line in file]

# Create a hash table using projection hashing
hash_table = ProjectionHashTable(len(identifiers))
for identifier in identifiers:
    hash_table.insert(identifier)

# Create an ordered list
ordered_list = OrderedList()
for identifier in identifiers:
    ordered_list.insert(identifier)
