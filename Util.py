# Util.py - Useful, Reusable Functions and Small Classes
from datetime import datetime
from math import ceil, floor
TS_FMT = '%Y%m%d_%H:%M:%S' # Timestamp Format
def NOW() -> datetime:
    return datetime.now()
def HumanReadable(ts: datetime) -> str:
    return ts.strftime(TS_FMT)
def HumanReadableNow() -> str:
    return HumanReadable(NOW())

def RoundToMultiple(number, multiple, direction='nearest'):
    # RoundToMultiple(): Round Number (Up, Down, Nearest) to Nearest Multiple.
    # Implementation: round(), ceil(), floor()
    # REF: https://datagy.io/python-round-to-multiple/
    if direction == 'up':
        return multiple * ceil(number / multiple)
    elif direction == 'down':
        return multiple * floor(number / multiple)
    else:
        return multiple * round(number / multiple)
if __name__ == '__main__':
    print(f'NOW: {HumanReadableNow()}')
