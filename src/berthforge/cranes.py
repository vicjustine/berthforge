"""Crane allocation across a terminal's berths.

A berth's throughput is limited by the cranes assigned to it. Each crane
moves a fixed number of containers per hour; a berth cannot be served by
more cranes than its rail length allows.
"""

CRANE_RATE_PER_HOUR = 26

BERTHS = {
    "B1": {"rail_slots": 3, "vessel_teu": 3800},
    "B2": {"rail_slots": 2, "vessel_teu": 2600},
    "B3": {"rail_slots": 4, "vessel_teu": 5200},
}


def cranes_for(berth: str, available: int) -> int:
    """Cranes actually assigned: limited by rail slots and by what is free."""
    if berth not in BERTHS:
        raise KeyError(f"unknown berth: {berth}")
    return min(BERTHS[berth]["rail_slots"], available)


def hours_to_discharge(berth: str, available: int) -> float:
    """Hours to move a vessel's boxes with the cranes that fit."""
    cranes = cranes_for(berth, available)
    if cranes == 0:
        raise ValueError("no cranes available")
    teu = BERTHS[berth]["vessel_teu"]
    return round(teu / (cranes * CRANE_RATE_PER_HOUR), 1)


def terminal_capacity(available: int) -> int:
    """Total containers per hour the terminal can move."""
    return sum(cranes_for(b, available) * CRANE_RATE_PER_HOUR for b in BERTHS)
