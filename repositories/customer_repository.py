# repositories/customer_repository.py

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
file_path = DATA_DIR / "customers.json"

def get_all_customers():
    
    with open(file_path) as f:
        return json.load(f)

def get_customer(customer_id):

    customers = get_all_customers()

    for customer in customers:
        if customer["customerId"] == customer_id:
            return customer

    return None