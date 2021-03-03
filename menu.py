"""
menu.py

The module provides Menu class.
Refer to Menu class documentation for more.
"""

import os
from itertools import zip_longest
from typing import List

from logistics import LogisticSystem
from order import Vehicle
from order import Order
from order import Item


class Menu:
    """
    A class used to represent a menu (a user interface to LogisticSystem).

    Run Menu().run() to use the provided interface.

    Attributes
    ----------
    logistics_system : list of vehicles
        a logistic system for wich menu is created
    options : dict
        possible options of menu along with functions corresponding to them

    Methods
    -------
    intro()
        print introduction to the user and return the vehicles created by user
    display_menu()
        print possible options to stdout
    run()
        run main loop of the menu
    list_vehicles()
        print all the vehicles in logistics system to stdout
    add_vehicle()
        ask user a vehicle and add it to logistics system
    list_orders()
        show user all the orders in logistics system
    add_order()
        ask user new order and add it to logistics system
    track_order()
        ask user an order id and print info about the corresponding order
    """
    def __init__(self) -> None:
        """Initialize menu with logistics system and options."""
        vehicles = self.intro()
        self.logistics_system = LogisticSystem(vehicles)
        self.options = {
            "1" : self.list_vehicles,
            "2" : self.add_vehicle,
            "3" : self.list_orders,
            "4" : self.add_order,
            "5" : self.track_order
        }

    def intro(self) -> List[Vehicle]:
        """Ask user the initial vehicles of logistics system and return them."""
        # ask number of vehicles
        while True:
            try:
                num_vehicles = int(input("Enter number of initial vehicles: "))
                assert num_vehicles >= 0
                break
            except (ValueError, AssertionError):
                print("You had to enter a positive integer.")

        # ask numbers of vehicles
        vehicles = []
        for num_vehicle in range(1, num_vehicles+1):
            if num_vehicle == 1:
                ending = "st"
            elif num_vehicle == 2:
                ending = "nd"
            elif num_vehicle == 3:
                ending = "rd"
            else:
                ending = "th"
            while True:
                try:
                    vehicle_no = int(input(f"Enter the number of {num_vehicle}{ending} vehicle: "))
                    assert vehicle_no > 0
                    vehicles.append(Vehicle(vehicle_no))
                    break
                except (ValueError, AssertionError):
                    print("You had to enter a postive integer.")
        return vehicles

    def display_menu(self) -> None:
        """Display an actual menu (with options) to user."""

        print("Logistics system menu")
        print()
        print("1. Show all vehicles")
        print("2. Add new vehicle")
        print("3. Show all orders")
        print("4. Place order")
        print("5. Track order")
        print("6. Quit")

    def run(self) -> None:
        """Repetedly ask user to enter an option.
        Use this method to enter user interface.
        """

        entered_invalid = False
        while True:
            os.system("cls") if os.name == "nt" else os.system("clear")
            self.display_menu()
            if entered_invalid:
                print("You've entered an invalid option.", end='')
            option = input("\nEnter an option: ")
            if option == '6':
                break
            action = self.options.get(option)
            if action:
                entered_invalid = False
                os.system("cls") if os.name == "nt" else os.system("clear")
                action()
                input("\nPress enter to continue...")
            else:
                entered_invalid = True

    def list_vehicles(self) -> None:
        """Show user (print to stdout) all the vehicles in logistics system."""

        if self.logistics_system.vehicles:
            print("The following are vehicles in logistics system: ")

            indent = 10
            space_btw_cols = 10
            max_length = max(map(lambda x: len(str(x.vehicle_no)), self.logistics_system.vehicles))
            max_length = max(len("Available"), len("Unavailable"), max_length)

            # print header
            print(indent*" " + f"{'Available': <{max_length}}"
                                        + " "*space_btw_cols + f"{'Unavailable': <{max_length}}")
            print(indent*" " + max_length*'-' + " "*space_btw_cols + "-"*max_length)

            # print columns
            available_vehicles = filter(lambda x: x.is_available,
                                                                    self.logistics_system.vehicles)
            unavailable_vehicles = filter(lambda x: not x.is_available,
                                                                    self.logistics_system.vehicles)
            available_vehicles = map(lambda x: x.vehicle_no,
                                            available_vehicles) #TODO: rewrite with operator module
            unavailable_vehicles = map(lambda x: x.vehicle_no,
                                        unavailable_vehicles) #TODO: rewrite with operator module
            for available_veh, unavailable_veh in zip_longest(available_vehicles,
                                                                unavailable_vehicles, fillvalue=""):
                print(indent*" " + f"{available_veh: <{max_length}}"
                                        + " "*space_btw_cols + f"{unavailable_veh: <{max_length}}")
        else:
            print("There are no vehicles yet.")

    def add_vehicle(self) -> None:
        """Ask user the number of new vehicle and add it to logistics system."""

        try:
            num = int(input("Enter number of new vehicle: "))
        except ValueError:
            print("You had to enter an integer.")
            return

        if num < 0:
            print("You had to enter a nonnegative integer.")
        else:
            #TODO: implement handling of collisions
            print(f"New vehicle with number {num} successfully added!")

            self.logistics_system.vehicles.append(Vehicle(num))

    def list_orders(self) -> None:
        """Show user all the orders in logistics system."""

        if self.logistics_system.orders:
            print("List of all orders in logistics system:")
            for idx, order in enumerate(self.logistics_system.orders, start=1):
                print(str(idx) + ") " + str(order))
        else:
            print("There are no orders created yet.")

    def add_order(self) -> None:
        """Ask user parameters of an order and add it to logistics system."""

        user_name = input("Enter user name: ")
        city = input("Enter city of destination point: ")

        while True:
            try:
                postoffice = int(input(f"Enter number of postoffice in {city}: "))
                assert postoffice > 0
                break
            except (ValueError, AssertionError):
                print("You had to enter a positive integer.")
        while True:
            try:
                num_items = int(input("Enter number of items to deliver: "))
                assert num_items >= 0
                break
            except (ValueError, AssertionError):
                print("You had to enter a nonnegative interger.")
        items = []
        for num_item in range(1, num_items+1):
            if num_item > 3:
                ending = "th"
            else:
                ending = "st" if num_item == 1 else "nd" if num_item == 2 else "rd"
            while True:
                try:
                    name = input(f"\nEnter name of the {num_item}{ending} item: ")
                    price = float(input(f"Enter price of the {num_item}{ending} item: "))
                    assert price >= 0
                    items.append(Item(name, price))
                    break
                except (ValueError, AssertionError):
                    print("You had to enter a nonnagative real number.")
        print()
        order = Order(user_name, city, postoffice, items)
        self.logistics_system.placeOrder(order)

    def track_order(self) -> None:
        """Ask user order id and print info about corresponding order if found."""

        # ask order_id
        while True:
            try:
                order_id = int(input("Enter id of an order to track: "))
                assert order_id >= 0
                break
            except (ValueError, AssertionError):
                print("You had to enter a nonnegative integer.")

        # track order
        self.logistics_system.trackOrder(order_id)


if __name__ == "__main__":
    Menu().run()
