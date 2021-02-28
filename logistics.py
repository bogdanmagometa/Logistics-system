import copy
from typing import List

from order import Vehicle
from order import Order


class LogisticSystem:
    def __init__(self, vehicles: List[Vehicle]) -> None:
        self.orders = []
        self.vehicles = copy.copy(vehicles)

    def place_order(self, order: Order) -> None:
        pass

    def track_order(self, order_id: int) -> str:
        pass
