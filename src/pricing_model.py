import numpy as np


def calculate_ticket_price(
    days_to_departure,
    remaining_seats,
    total_seats=180,
    base_price=100
):
    """
    Estimate a ticket price using time-to-departure
    and remaining seat inventory.
    """

    if days_to_departure < 0:
        raise ValueError("Days to departure cannot be negative.")

    if remaining_seats < 0 or remaining_seats > total_seats:
        raise ValueError("Remaining seats must be between 0 and total seats.")

    occupancy_rate = 1 - (remaining_seats / total_seats)

    # Price pressure caused by limited remaining capacity
    capacity_effect = 120 * occupancy_rate

    # Price pressure as the departure date approaches
    time_effect = 80 * np.exp(-days_to_departure / 30)

    estimated_price = base_price + capacity_effect + time_effect

    return round(estimated_price, 2)


if __name__ == "__main__":
    price = calculate_ticket_price(
        days_to_departure=10,
        remaining_seats=40
    )

    print(f"Estimated ticket price: ${price}")
