"""
order.py

This module contains classes needed for emulating logistics system. In particular, the following
classes are here:
Item
Vehicle
Order
Location
"""

import copy
from typing import List


class Item:
    """A class used to represent an item for logistics system.
    
    Attributes
    ----------
    name : str
        a name of the item, e.g. book, letter, TV, cookie
    price : float
        the price of an item in UAH
    """
    def __init__(self, name: str, price: float) -> None:
        """Initialize Item with name and price (in UAH).

        >>> item = Item("phone", 5123.4567)
        >>> item.name
        'phone'
        >>> item.price
        5123.4567
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Return human-readable representation of the order.

        >>> item = Item("shoes", 240)
        >>> print(item)
        The item with name shoes and price 240
        """
        return f"The item with name {self.name} and price {self.price}"


class Vehicle:
    """A class user to represent Vehicles for logistics system.

    Attributes
    ----------
    vehicle_no : int
        number of vehicle
    is_available : bool
        tells if a vehicle is available for delivering
    """
    def __init__(self, vehicle_no: int) -> None:
        """Initialize Vehicle with vehicle number."""
        self.vehicle_no = vehicle_no
        self.is_available = True


class Order:
    """A class used to represent an order in logistics system.

    Attributes
    ----------
    user_name : str
        the name of the user who created the order
    city : str
        the city of destination
    postoffice : int
        the postoffice number of Ukrposhta in the city
    items : list of items
        items listed in the order
    location : Location
        location of destination point
    vehicle : Vehicle
        vehicle for delivery of the item
    """
    num_orders_created = 0

    def __init__(self, user_name: str, city: str, postoffice: int, items: List[Item]) -> None:
        """Initialize order with name of user, delivery city, postoffice, and items to deliver.

        >>> order = Order("Bohdan", "Stryi", 2,
        ... [Item('Arduino',120), Item("ESP32-CAM",200), Item("Raspberri Pi Zero",1100)])
        Your order number is 0.
        >>> isinstance(order.location, Location)
        True
        >>> order.vehicle
        >>> order.user_name
        'Bohdan'
        >>> order.location.city
        'Stryi'
        >>> order.location.postoffice
        2
        >>> all(map(lambda x: isinstance(x, Item), order.items))
        True
        """
        self.order_id = Order.num_orders_created
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = copy.copy(items)
        self.vehicle = None
        Order.num_orders_created += 1
        print(f"Your order number is {self.order_id}.")

    def __str__(self) -> str:
        """Return human-readable represenation of an order.
        
        >>> order = Order("Ivan", "Kyiv", "42", ['computer'])
        Your order number is 1.
        >>> print(order)
        The order #1 by Ivan to city Kyiv, postoffice 42. The item is computer.
        """
        text = f"The order #{self.order_id} by {self.user_name} to city {self.location.city}, post\
office {self.location.postoffice}."

        if self.items:
            text += " The item"
            if len(self.items) == 1:
                return text + f" is {self.items[0]}."
            return text + f"s are {', '.join(self.items)}."
        return text

    def calculate_amount(self) -> float:
        """Return total cost of each Item (in UAH).

        >>> order = Order("Bohdan", "Stryi", "2",
        ... [Item('Arduino',120), Item("ESP32-CAM",200),
        ... Item("Raspberri Pi Zero",1100)]) #doctest: +ELLIPSIS
        Your order number is ....
        >>> order.calculate_amount()
        1420
        """
        return sum(item.price for item in self.items)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        """Assign a vehicle to an order.

        >>> order = Order("Oksana", "Zhytomyr", 5, [Item("cap", 100)]) #doctest: +ELLIPSIS
        Your order number is ....
        >>> vehicle = Vehicle(213)
        >>> order.assign_vehicle(vehicle)
        >>> order.vehicle.vehicle_no
        213
        """
        self.vehicle = vehicle


class Location:
    """A class used to represent a location in logistics system.

    Attributes
    ----------
    city : str
        city of the location
    postoffice : int
        number of postoffice of Ukrposhta in city
    """
    def __init__(self, city: str, postoffice: int) -> None:
        """Initialize location with delivery city and postoffice.

        >>> location = Location("Nezhukhiv", 1)
        >>> location.city
        'Nezhukhiv'
        >>> location.postoffice
        1
        """
        self.city = city
        self.postoffice = postoffice


if __name__ == "__main__":
    import doctest
    doctest.testmod()
