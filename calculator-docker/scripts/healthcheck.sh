#!/bin/sh
# Check if the app ran successfully (creative twist: check logs)
if grep -q "Result" /var/log/calculator.log; then
  exit 0
else
  exit 1
fi