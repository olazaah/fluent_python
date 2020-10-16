# Dictionaries and Sets are implemented with Hash Tables and they are highly optimised

# Using isinstance() is better than checking if a function argument is of a particular type

# What is Hashable? An Object is hashable if it has a hash value which never changes during it's lifetime( it needs a __hash__() method) and can be compared to other objects (it needs an __eq__() method)
# Atomic immutable types are all hashable e.g (str, bytes, numeric types) tuple is hashable if all the items are hashable

# using dict comprehension

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
for i in range(3):
    print()
print({code: country.upper() for country, code in country_code.items() if code < 66})


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


my_dict = StrKeyDict0()
print(my_dict.get('1'))

import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item


my_dict = StrKeyDict()
my_dict['1'] = 1
print(my_dict[1])
