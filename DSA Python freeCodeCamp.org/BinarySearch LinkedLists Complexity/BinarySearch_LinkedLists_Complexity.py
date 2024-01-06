p1 = {'name': 'John Doe',
      'sex': 'Male',
      'age': 32,
      'married': True,
      'address': '1, Penny Lane'}

list_of_keys = list(p1.keys())
for i in list_of_keys:
    print(i)

list_of_values = list(p1.values())
for i in list_of_values:
    print(i)

list_of_key_val_pairs = list(p1.items())
for i in list_of_key_val_pairs:
    print(i)
