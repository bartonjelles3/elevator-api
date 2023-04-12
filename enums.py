"""Standardize important values."""

from enum import Enum

class State(str, Enum):
  IDLE = "IDLE"
  MOVING = "MOVING"
  MALFUNCTIONING = "MALFUNCTIONING"

class Direction(str, Enum):
  UP = "UP"
  DOWN = "DOWN"

class Status(str, Enum):
  SUCCESS = "SUCCESS"
  FAILIRE = "FAILIRE"