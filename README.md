### Vendor Management System with Performance Metrics

This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Table of Contents

- [Core Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
## Core Features

### 1. Vendor Profile Management:
         The system stores vendor information including name, contact details, address, and a unique vendor code.
         
### 2. Purchase Order Tracking:
        Purchase orders are tracked with fields like PO number, vendor reference, order date, items, quantity, and status.
        
### 3. Vendor Performance Evaluation:
        Calculate vendor performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.   


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vendor-management-system.git

   ```
2. Create a virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```
5. Access the application at http://localhost:8000.

