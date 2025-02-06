from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="cdr_analysis")

def get_location(phone_number):
    # Simulating lookup
    return geolocator.geocode("New York, USA")
