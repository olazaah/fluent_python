# The actual bytes that represents a character depends on the encoding in use. An encoding is an algorithm that coverts code points to byte e.g UTF-8 encoding
# Coverting from code points to byte is encoding and from byte to code point is decoding

s = 'café'
print(len(s))
b = s.encode('utf-8')
print(b)
print(len(b))
print(b.decode('utf-8'))

# A 5 byte sequence as byte and as bytearray
[print() for i in iter(range(3))]

cafe = bytes('caf é', 'utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])
print([cafe_arr[i] for i in iter(range(len(cafe_arr)))])

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

print(chr(32), 'something')

