def type_detective():
    """Investigate data types."""
    data = [42, 3.14, "hello", True, None]

    for item in data:
        item_type = type(item).__name__
        is_string = isinstance(item, str)
        
        print(f"Value: {item!r}")
        print(f"  Type: {item_type}")
        print(f"  Is it a string? {is_string}")
        print()

def equality_vs_identity():
    """Demonstrate == vs is."""
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print()
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")
    print(f"a == c: {a == c}")
    print(f"a is c: {a is c}")
    print()
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    print(f"id(c) = {id(c)}")
    
def mutable_trap():
    """The bug that gets developers fired."""
    original = [1, 2, 3]

    # DANGEROUS: alias points to the SAME list
    alias = original
    alias.append(4)

    print("After alias.append(4):")
    print(f"alias = {alias}")
    print(f"original = {original}")   # What do you expect?
    print()

    # SAFE: copy is a DIFFERENT list
    original2 = [1, 2, 3]
    copy = original2.copy()   # Creates a NEW list with same values
    copy.append(4)

    print("After copy.append(4):")
    print(f"copy = {copy}")
    print(f"original2 = {original2}")  # What do you expect?


if __name__ == "__main__":
    type_detective()
    print("\n" + "="*50 + "\n")
    equality_vs_identity()
    print("\n" + "="*50 + "\n")
    mutable_trap()