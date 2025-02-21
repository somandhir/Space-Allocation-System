# AI Shelf Predictor Backend

## Overview
The **AI Shelf Predictor Backend** is part of the **Space Allocation System**, designed to automate retail shelf space allocation using historical sales data, product demand, and customer preferences. This backend processes data and provides optimized shelf arrangements based on insights.

## Features
- **Automated Allocation Predictions**: Uses historical sales data to predict optimal shelf space allocation.
- **Data Processing & Analysis**: Implements algorithms to analyze sales trends and maximize retail efficiency.
- **Multiple Output Types**: Generates various outputs, including:
  - Graphical representation of shelf allocations.
  - Prediction of item shelf-space percentage based on profit and sales frequency.

## Getting Started
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies (install via `requirements.txt` if applicable)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/AI-Shelf-Predictor-Backend.git
   cd AI-Shelf-Predictor-Backend
   ```
2. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

### Usage
To start the predictor, run:
```bash
python app.py
```
This will start the training program and provide an endpoint URL.

### Accessing Results
Once the training completes, the endpoint will be available. Access it via:
- **Browser**: Enter the provided URL.
- **Postman**: Send a GET request to the URL.

The response will include:
- **Graphical Analysis**
- **Shelf-space allocation predictions** based on profitability and sales frequency.

## Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request with improvements.


## Contact
For queries or suggestions, reach out via somandhir@gmail.com

