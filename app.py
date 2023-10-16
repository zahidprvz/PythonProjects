import phonenumbers
from phonenumbers import geocoder, carrier, national_significant_number, can_be_internationally_dialled, number_type

# Parse the phone number
number = "+923256032363"
parsed_number = phonenumbers.parse(number, "PK")

# Get the location of the phone number
location = phonenumbers.geocoder.description_for_number(parsed_number, "en")
print("\nLocation:", location)

# Get the name of the service provider
service_provider = phonenumbers.carrier.name_for_number(parsed_number, "en")
print("\nService Provider:", service_provider)

# Get the NSN 
nsn = phonenumbers.national_significant_number(parsed_number)
print("\nNSN: ", nsn)

# International Dialing
dailing = phonenumbers.can_be_internationally_dialled(parsed_number)
print("\nDialing: ", dailing)

# Number Type
type = phonenumbers.number_type(parsed_number)
print("\nNumber Type: ", type)

# Short Number Info
formatting = phonenumbers.format_number_for_mobile_dialing(parsed_number, "en" ,True)
print("\nWith Formatting: ", formatting)


