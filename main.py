from ecosystem import *
from time import sleep

DAYS_SIMULATED = 20
RIVER_SIZE = 15
START_BEARS = 10
START_FISH = 15

def BearFishRiver():

  r = River(RIVER_SIZE, START_BEARS, START_FISH)
  day = 0
  done = False
  for day in range(DAYS_SIMULATED):
    print(f"\n\nDay: {day+1}")
    print(r)
    print(f"\nStarting Poplation: {r.population} animals")
    done = r.new_day()
    print(f"Ending Poplation: {r.population} animals")
    print(r)
    day += 1
    sleep(3)
    if r.population == RIVER_SIZE**2:
      print("⚠️ ⚠️ ⚠️  Population Capacity Reached")
      break



if __name__ == "__main__":
  BearFishRiver()