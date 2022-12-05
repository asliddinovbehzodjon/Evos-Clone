from geopy.geocoders import Nominatim
def get_location(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(latitude) + "," + str(longitude))
    return location.address