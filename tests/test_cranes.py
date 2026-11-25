import pytest
from berthforge.cranes import (
    cranes_for, hours_to_discharge, terminal_capacity, CRANE_RATE_PER_HOUR,
)


def test_rail_slots_cap_assignment():
    assert cranes_for("B2", 10) == 2


def test_availability_caps_assignment():
    assert cranes_for("B3", 1) == 1


def test_discharge_hours_B1_full():
    assert hours_to_discharge("B1", 3) == 48.7


def test_discharge_hours_B3_full():
    assert hours_to_discharge("B3", 4) == 50.0


def test_terminal_capacity_unconstrained():
    assert terminal_capacity(9) == 9 * CRANE_RATE_PER_HOUR


def test_unknown_berth():
    with pytest.raises(KeyError):
        cranes_for("B9", 2)
