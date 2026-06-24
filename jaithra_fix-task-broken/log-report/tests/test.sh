#!/bin/bash

# Create the required verifier log directory
mkdir -p /logs/verifier

# pytest and pytest-json-ctrf are baked into the environment image.
# Generate the CTRF payload where Harbor expects it.
pytest /tests/test_outputs.py -rA --json-ctrf=/logs/verifier/ctrf.json

# Report the final binary reward to the correct Harbor path.
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi