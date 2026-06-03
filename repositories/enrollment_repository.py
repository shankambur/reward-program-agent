import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
file_path = DATA_DIR / "enrollments.json"

def get_all_enrollments():
    with open(file_path) as f:
        return json.load(f)

def get_enrollments_by_customer(customer_id):

    enrollments = get_all_enrollments()
    enrollments_by_customer = []
    for enrollment in enrollments:
        if enrollment["customerId"] == customer_id:
                enrollments_by_customer.append(enrollment)

    return enrollments_by_customer

def get_enrollments_by_offer(offer_id):

    enrollments = get_all_enrollments()
    enrollments_by_offer = []
    for enrollment in enrollments:
        if enrollment["offerId"] == offer_id:
            enrollments_by_offer.append(enrollment)

    return enrollments_by_offer

def is_customer_enrolled(customer_id, offer_id):

    enrollments = get_all_enrollments()

    for enrollment in enrollments:
          if enrollment["customerId"] == customer_id and enrollment["offerId"] == offer_id:
            return True

    return False