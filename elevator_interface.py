"""Elevator control interface."""

import elevator_logic
from utils import State, Status

ELEVATOR_ATTRS = elevator_logic.elevator_attrs

def call_and_wait(floor):
  """Call the elevator. If there's a malfunction via await_elevator, call 
  again. Await elev"""
  arrived = False
  while not arrived:
    elevator = elevator_logic.choose_elevator(floor)
    ELEVATOR_ATTRS[elevator]["destination_floor"] = floor
    ELEVATOR_ATTRS[elevator]["state"] = State.MOVING
    arrived = elevator_logic.await_elevator(elevator)
  return Status.SUCCESS

def dest_and_wait(currentElevator, floor):
  # Could maybe be combined with call_elevator.
  ELEVATOR_ATTRS[currentElevator]["destination_floor"] = floor
  ELEVATOR_ATTRS[currentElevator]["state"] = State.MOVING
  arrived = elevator_logic.await_elevator(currentElevator)
  if arrived:
    return Status.SUCCESS
  else:
    return Status.FAILIRE

def get_status(elevator, all_elevators, all_attrs):
  "Get either all attrs or just states of all or individual elevator."
  # Could use 'schedule' to log routinely as a simple solution. Would need to
  # maybe monitor minutes in certain states to see if there's an issue.
  if all_attrs:
    if all_elevators:
      return ELEVATOR_ATTRS
    return {elevator: ELEVATOR_ATTRS[elevator]}
  
  if all_elevators:
    status = {}
    for elevator_id, attrs in ELEVATOR_ATTRS.items():
      status[elevator_id] = attrs["state"]
    return status
  return {elevator: ELEVATOR_ATTRS[elevator]["state"]}
  

