"""Elevator control logic.

Acutal control is of course abstracted away. In reality we would probably
interfacr with some sort of hardware interface that would tell us what floor
we are at, etc."""

import time
import random
import logging

from utils import State, Direction

# Use a DB. 
elevator_attrs = {
    1: {
        "current_floor": 1,
        "destination_floor": 1,
        "state": State.IDLE,
        "direction": None
    },
    2: {
        "current_floor": 1,
        "destination_floor": 1,
        "state": State.IDLE,
        "direction": None
    }
}

def choose_elevator(floor):
  """Simple elevator choice. Try and use idle, else use closest."""
  closest_dest, closest_id = 0, 0
  for elevator_id, attrs in elevator_attrs.items():
    state = attrs["state"]
    dest = attrs["destination_floor"]
    if state == State.MALFUNCTIONING:
      continue
    if state == State.IDLE:
      return elevator_id
    # TODO: Add queue to elevators. This will overwrite the previous request.
    floor_dif = abs(floor - dest)
    if closest_dest > floor_dif:
      closest_dest, closest_id = floor_dif, elevator_id

  return closest_id

def await_elevator(elevator):
  """Try and emulate awaiting an elevator. Change current floor to be closer
  to dest every .1s."""
  current_floor = elevator_attrs[elevator]["current_floor"]
  destination_floor = elevator_attrs[elevator]["destination_floor"]
  direction = elevator_attrs[elevator]["direction"]
  failureNum = random.random()

  for _ in range(abs(destination_floor - current_floor)):
    time.sleep(.1)
    # Simulates an elevator failure based on chance.
    if failureNum < 0.1:
      elevator_attrs[elevator]["state"] = State.MALFUNCTIONING
      elevator_attrs[elevator]["destination_floor"] = current_floor
      elevator_issue(elevator)
      return False
    if direction == Direction.UP:
      elevator_attrs[elevator]["current_floor"] += 1
    else:
      elevator_attrs[elevator]["current_floor"] -= 1

  elevator_attrs[elevator]["state"] = State.IDLE
  return True
    
def elevator_issue(elevator):
  # Very rudimentary. Use Datadog, etc. for alerting in this situation.
  # Or hire somebody to monitor logs 24/7. :p (wait that's us)
  logging.error(f"Elevator {elevator} has experienced a malfunction. Current "
                f"attribures: {elevator_attrs[elevator].values()}")