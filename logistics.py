"""
logistics.py

A module for a single class LogisticSystem.
Refer to LogisticSystem documentation for more information.
"""

import copy
from typing import List

from order import Vehicle
from order import Order


class LogisticSystem:
    """
    A class used to represent logistics system.

    Attributes
    ----------
    orders : list of orders
        all orders known to logistics system
    vehicles : list of vehicles
        all vehicles known to logistics system

    Methods
    -------
    placeOrder(order)
        assign an order a vehicle>>> from order import *
    trackOrder(order_id)
        print information about an order with passed order id
    """
    def __init__(self, vehicles: List[Vehicle]) -> None:
        """Initialize logistics system with vehicles andd orders (empty list).
        
        >>> vehicles = [Vehicle(1), Vehicle(10)]
        >>> logistics_sys = LogisticSystem(vehicles)
        >>> logistics_sys.placeOrder(Order("Bohdan", "Lviv", 2, [Item("Arduino", 200)]))
        Your order number is 0.
        >>> logistics_sys.trackOrder(0)
        Your order #0 is sent to Lviv. Total price: 200 UAH.
        """
        self.orders = []
        self.vehicles = copy.copy(vehicles)

    def placeOrder(self, order: Order) -> None:
        """Assign a vehicle to an order and add an order to orders of logistics system.

        >>> vehicles = [Vehicle(1)]
        >>> logistics_sys = LogisticSystem(vehicles)
        >>> logistics_sys.placeOrder(Order("Jack", "London", 4, [Item("Arduino mega", 200)]))
        Your order number is 1.
        >>> logistics_sys.placeOrder(Order("Tom", "Kyiv", 31, [Item("Cap", 120)]))
        Your order number is 2.
        There is no available vehicle to deliver an order.
        >>> logistics_sys.orders #doctest: +ELLIPSIS
        [<order.Order object at 0x...>]
        """
        try:
            vehicle = next(vehicle for vehicle in self.vehicles if vehicle.is_available)
            order.assign_vehicle(vehicle)
            self.orders.append(order)
            vehicle.is_available = False
        except StopIteration:
            print("There is no available vehicle to deliver an order.")

    def trackOrder(self, order_id: int) -> str:
        """Print information (order id, city of delivery, price in UAH) about the order with passed
        in order id.

        >>> vehicles = [Vehicle(1)]
        >>> logistics_sys = LogisticSystem(vehicles)
        >>> logistics_sys.placeOrder(Order("Jack", "London", 4, [Item("Arduino mega", 200)]))
        Your order number is 3.
        >>> logistics_sys.trackOrder(3)
        Your order #3 is sent to London. Total price: 200 UAH.
        """
        try:
            order = next(order for order in self.orders if order.order_id == order_id)
            order_id = order.order_id
            city = order.location.city
            amount = order.calculate_amount()
            print(f"Your order #{order_id} is sent to {city}. Total price: {amount} UAH.")
        except StopIteration:
            print("No such order.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
