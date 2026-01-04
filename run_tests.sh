#!/bin/bash

# Activate virtual environment
source venv/bin/activate   # Use venv/Scripts/activate on Windows

# Run the test suite
pytest

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
