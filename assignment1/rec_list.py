class Node:  # Node list is None or Node(value, rest), where rest is the rest of the list
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Node)
                and self.value == other.value
                and self.rest == other.rest
                )

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.value, self.rest)
    # a StrList is one of
    # - None, or
    # - Node(string, StrList)
    # StrList -> string
    # Returns first (as determined by Python compare) string in StrList
    # If StrList is empty.txt (None), return None # Must be implemented recursively

    def first_string(strlist):
        if strlist is None:
            return None
        min_rest = first_string(strlist.rest)
        if min_rest is None or strlist.value < min_rest:
            return strlist.value
        return min_rest


if __name__ == "__main__":
    node = Node(3, None)
    print(node)