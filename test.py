import hashids

hashids = hashids.Hashids(salt="fasisme123")
id = hashids.encode(1)
numbers = hashids.decode(id)
print(numbers)
print(id)
