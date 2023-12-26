# dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'}) #yeni eleman ekleme/güncelleme.
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China') #eleman silme
capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany')) #return the value for key if key is in the dictionary, else default.
#print(capitals.keys()) #it prints only the keys and not the values.
#print(capitals.values()) #it prints only the values.
#print(capitals.items()) #this will print entire dictionary.

for key, value in capitals.items():
    print(key, value)