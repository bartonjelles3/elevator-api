"Flask app for implementing a web API controlling elevators."

from flask import Flask, request, jsonify

import elevator_interface
from enums import Status

app = Flask(__name__)

@app.route("/call_elevator", methods=["POST"])
def call_elevator():
    request_data = request.get_json()
    floor = request_data.get("floor")

    result = elevator_interface.call_and_wait(floor)
    if result == Status.SUCCESS:
      return jsonify({"message": "Elevator arrived at your floor."})

@app.route("/set_destination", methods=["POST"])
def set_destination():
    request_data = request.get_json()
    elevator = request_data.get("elevator")
    floor = request_data.get("floor")

    result = elevator_interface.dest_and_wait(elevator, floor)
    if result == Status.SUCCESS:
      return jsonify({"message": "Elevator arrived at your destination."})
    else:
      return jsonify({"message": "Elevator malfunctioned. Mgmt alerted."})

@app.route("/get_status", methods=["GET"])
def get_status():
    request_data = request.get_json()
    elevator = request_data.get("elevator", 1)
    all_elevators = request_data.get("all_elevators", False)
    all_attrs = request_data.get("all_attrs", False)

    result = elevator_interface.get_status(elevator=elevator, all_elevators=all_elevators, all_attrs=all_attrs)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
