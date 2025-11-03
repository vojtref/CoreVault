a = int(input()) # Vstup v sekundach

SECS_IN_MIN = 60
SECS_IN_HOUR = 60 * SECS_IN_MIN
SECS_IN_DAY = 24 * SECS_IN_HOUR

d = a // SECS_IN_DAY
h = (a % SECS_IN_DAY) // SECS_IN_HOUR
m = (a % SECS_IN_HOUR) // SECS_IN_MIN
s = (a % SECS_IN_MIN)

print(f"{d}d{h}h{m}m{s}s")