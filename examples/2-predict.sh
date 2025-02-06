#!/bin/bash

echo "Running prediction using HuBiCEM model..."

# Run prediction
python src/predict.py

echo "Prediction complete. Check 'prediction.csv' and 'report.txt'."
