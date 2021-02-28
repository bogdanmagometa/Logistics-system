import copy
from typing import List


class Item:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        print(f"The item with name {self.name} and price {self.price}")


class Order:
    num_orders_created = 0

    def __init__(self, user_name: str, city: str, post_office: int, items: List[Item]) -> None:
        self.order_id = num_orders_created
        self.user_name = user_name
        self.location = Location(city, post_office)
        self.items = copy.copy(items)
        self.vehicle = None
        num_orders_created += 1

    def __str__(self) -> str:
        return f"The order #{self.order_id} by {self.user_name} to city {self.location.city}, post\
office {self.location.post_office}. The items are {','.join(self.items)}."

    def calculate_amount(self) -> float:
        return sum(item.price for item in self.items)

    def assign_vehicle(self, vehicle: Vehicle) -> None:
        self.vehicle = vehicle


class Vehicle:
    def __init__(self, vehicle_no: int, is_available: bool) -> None:
        self.vehicle_no = vehicle_no
        self.is_available = is_available


class Location:
    def __init__(self, city: str, post_office: int) -> None:
        self.city = city
        self.post_office = post_office
