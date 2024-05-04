### Vendor Management System with Performance Metrics

This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Table of Contents

- [Core Features](#features)
- [Tech Stack](#techstack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [API Documentation](#apidocumentation)
## Core Features

### 1. Vendor Profile Management:
         The system stores vendor information including name, contact details, address, and a unique vendor code.
         
### 2. Purchase Order Tracking:
        Purchase orders are tracked with fields like PO number, vendor reference, order date, items, quantity, and status.
        
### 3. Vendor Performance Evaluation:
        Calculate vendor performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.   

## Tech Stack

**Stack:** Python, Django, dbsqlite3

**Server:** localhost:8000        


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Vendor_Management.git

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
5. Access the application at http://127.0.0.1:8000/.

## API Endpoints

Below is a summary of the available API endpoints:

**Vendor Profile Management**

| Endpoint               | Method      | Description                           |
| ---------------------- | ----------- | ------------------------------------- |
| `/api/vendors-create/`      | POST        | Create a new vendor.                  |
| `/api/vendors-list/`      | GET         | List all vendors.                     |
| `/api/vendors-retrieve/{id}/` | GET         | Retrieve a specific vendor's details. |
| `/api/vendors-update/{id}/` | PUT / PATCH | Update a vendor's details.            |
| `/api/vendors-delete/{id}/` | DELETE      | Delete a vendor.                      |

**Purchase Order Tracking**

| Endpoint                                  | Method       | Description                                    |
| ----------------------------------------- | ------------ | ---------------------------------------------- |
| `/api/purchase_orders-create/`                 | POST         | Create a purchase order.                       |
| `/api/purchase_orders-list/`                 | GET          | List all purchase orders.                      |
| `/api/purchase_orders-retrieve/{id}/`            | GET          | Retrieve details of a specific purchase order. |
| `/api/purchase_orders-update/{id}/`            | PUT / PATCH  | Update a purchase order.                       |
| `/api/purchase_orders-delete/{id}/`            | DELETE       | Delete a purchase order.                       |
| `/api/purchase_orders/{id}/acknowledge/` | PUT / PATCH | Acknowledge a purchase order.                  |

**Vendor Performance Evaluation**

| Endpoint                                  | Method | Description                              |
| ----------------------------------------- | ------ | ---------------------------------------- |
| `/api/vendors/{id}/performance`         | GET    | Retrieve a vendor's performance metrics. |
| `/api/performance-retrieve/<int:pk>/performance/` | GET    | Retrieve a vendor's historical performance. |

## Testing

1. **Install Postman:** Download and install Postman from (https://www.postman.com/downloads/).

2. **Send Requests:**
   - Open Postman and create a new request.
   - Enter the API endpoint URL and choose the appropriate HTTP method.
   - Add any required headers and request body data.
   - Click "Send" to execute the request.

3. **Review Responses:**
   - Postman will display the response from the server, including status codes and data.
   - Review the response to ensure it matches the expected behavior of your API.

4. **Repeat:**
   - Test other API endpoints by creating new requests in Postman.

By following these steps, you can effectively test your API endpoints using Postman and verify their functionality.

## API Documentation:

For detailed API documentation and usage instructions, refer to the https://docs.djangoproject.com/en/5.0/ and https://www.django-rest-framework.org/ file.

