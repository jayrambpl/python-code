import phonenumbers
import db as phoneNumber
import opencage
import folium

from opencage.geocoder import OpenCageGeocode


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(phoneNumber.phoneNumber)

location = geocoder.description_for_number(pepnumber, "en")

from phonenumbers import carrier

service_provider = phonenumbers.parse(phoneNumber.phoneNumber)

print(location)

print(service_provider)

from phonenumbers import timezone

key = "cd570a2360f546b4910ce332e07f32fa"

geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lnt = results[0]['geometry']['lng']

print(lat, lnt)

print(timezone.time_zones_for_number(pepnumber))

from phonenumbers import carrier

service_provider = phonenumbers.parse(phoneNumber.phoneNumber)

print(carrier.name_for_number(service_provider, "en"))

mymap = folium.Map(location=[lat, lnt], zoom_start=9)

folium.Marker([lat, lnt], popup=location).add_to((mymap))

# save map as html file
mymap.save("mylocation.html")

print(results)

print(results[0]['formatted'])

# print(results[0]['components']['city'])

# print(results[0]['components']['country'])

# print(results[0]['components']['state'])

# print(results[0]['components']['county'])

# print(results[0]['components']['postcode'])

# print(results[0]['components']['road'])

# print(results[0]['components']['house_number'])

# print(results[0]['components']['neighbourhood'])

# print(results[0]['components']['suburb'])

# print(results[0]['components']['village'])

# print(results[0]['components']['suburb'])




