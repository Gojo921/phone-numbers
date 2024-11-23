import phonenumbers
from phone import number
from phonenumbers import geocoder
from phonenumbers import carrier

# country history  CH
ch_nmbr = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmbr, "en"))

# service provider for the number
service_nmbr = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmbr, "en"))