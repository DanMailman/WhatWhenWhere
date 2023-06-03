# Util.py - Useful, Reusable Functions and Small Classes
from datetime import datetime
from math import ceil, floor
TS_FMT = '%Y%m%d_%H:%M:%S' # Timestamp Format
def NOW() -> datetime:
    # NOW(): Return datetime of current system clock.
    # Implementation: call to now()
    return datetime.now()
def HumanReadable(ts: datetime) -> str:
    # HumanReadable(): Returns Human Readable Representation of datetime object
    # Implementation: call to strftime
    return ts.strftime(TS_FMT)
def HumanReadableNow() -> str:
    # HumanReadableNow(): Return Human Readable Representation of current system clock.
    # Implementation: HumanReadable() on NOW()
    return HumanReadable(NOW())
def RoundToMultiple(number: float, multiple: float , direction: str ='nearest') -> float:
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
    print(f'RoundToMultiple({53.12},{10}):          {RoundToMultiple(53.12,10)}')
    print(f'RoundToMultiple({53.12},{10}, nearest): {RoundToMultiple(52.12, 10,"nearest")}')
    print(f'RoundToMultiple({53.12},{10}, up):      {RoundToMultiple(52.12, 10,"up")}')
    print(f'RoundToMultiple({53.12},{10}, down):    {RoundToMultiple(52.12, 10,"down")}')
    print(f'RoundToMultiple({53.12},{.10}):          {RoundToMultiple(53.12,.10)}')
    print(f'RoundToMultiple({53.12},{.10}, nearest): {RoundToMultiple(52.12, .10,"nearest")}')
    print(f'RoundToMultiple({53.12},{.10}, up):      {RoundToMultiple(52.12, .10,"up")}')
    print(f'RoundToMultiple({53.12},{.10}, down):    {RoundToMultiple(52.12, .10,"down")}')
    #print(f'RoundToMultiple({53.12},{1}):  {RoundToMultiple(52.12,10)}')
