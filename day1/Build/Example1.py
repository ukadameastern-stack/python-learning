from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_availability(self):
        pass

    @abstractmethod
    def create_booking(self):
        pass


# -------------------------------

class HotelProvider(BaseProvider):

    def get_availability(self):
        return "Rooms available: 101, 102"

    def create_booking(self):
        return "Hotel room booked successfully"


# -------------------------------

class FlightProvider(BaseProvider):

    def get_availability(self):
        return "Flights available: AI101, AI202"

    def create_booking(self):
        return "Flight booked successfully"


# -------------------------------

hotel = HotelProvider()

print(hotel.get_availability())
print(hotel.create_booking())
'''
Rooms available: 101, 102
Hotel room booked successfully
'''


flight = FlightProvider()

print(flight.get_availability())
print(flight.create_booking())
'''
Flights available: AI101, AI202
Flight booked successfully
'''