# Car Recommendation System

This is a simple Python project that recommends a car based on user preferences such as engine power, mileage, seating capacity, and price.

## Features

- Stores car details in a CSV file
- Reads user preferences from input
- Filters and recommends the best-matching car
- Supports cars from Toyota, Hyundai, Maruti Suzuki, and Audi

## Car Details Stored

Each car entry includes:

- Company Name
- Model Name
- Engine Power (in cc)
- Mileage (in kmpl)
- Seating Capacity
- Price (in lakhs)
- Available Colours

## How It Works

1. The script creates a CSV file `Cars_details.csv` with all car records.
2. It asks the user to input:
   - Minimum engine power
   - Minimum mileage
   - Minimum seating capacity
   - Maximum budget
3. The program then reads the file and finds the first car that matches the criteria.

## Requirements

- Python 3.x
- Uses built-in `csv` module only

## How to Run

1. Save the code in a file, for example `car_recommendation.py`.
2. Run the file using a terminal or Python IDE

## File Overview

- `Cars_details.csv` – CSV file that stores all car information
- `car_recommendation.py` – Python script for car selection based on inputs
