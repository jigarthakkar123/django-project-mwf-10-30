myset = set(["a", "b", "c"])
print(myset)

myset.add("d")
print(myset)

myset.add("a")
print(myset)


normal_set = set(["a", "b","c"])
print("Normal Set")
print(normal_set)
normal_set.add("abc")
print(normal_set)

frozen_set = frozenset(["e", "f", "g"]) 
print("\nFrozen Set")
print(frozen_set)

