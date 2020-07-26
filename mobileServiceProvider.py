# Mobile service provider name using python

import phonenumbers
from phonenumbers import carrier

mobile_no = input("The phone number(with country code) is: ")
serviceProvider = phonenumbers.parse(mobile_no)
serProvName = carrier.name_for_number(serviceProvider, 'en')
print(serProvName)