# berthforge

Crane allocation for a container terminal. Works out how many cranes a berth
can take, how long a vessel takes to discharge, and the terminal's hourly
capacity.

## Berths

| Berth | Rail slots | Vessel |
|---|---|---|
| B1 | 3 | 3,800 TEU |
| B2 | 2 | 2,600 TEU |
| B3 | 4 | 5,200 TEU |

A crane moves 26 containers per hour.

## Tests

```
pytest -q
```
## Note
The berthbox failed because the image was not build by berthbox. but passed for berthforge because it was built by it. 
