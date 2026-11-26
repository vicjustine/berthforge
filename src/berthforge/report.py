""" Print the terminal's crane allocation summary. """

from berthforge.cranes import BERTHS, hours_to_discharge, terminal_capacity


def main() -> None: 
    available = 9 
    print(f"berths: {len(BERTHS)}")
    for berth in sorted(BERTHS): 
        hours = hours_to_discharge(berth, available)
        print(f" {berth}: {hours} h")
    print(f"capacity: {terminal_capacity(available)} boxes/h")

if __name__ == "__main__": 
    main() 
