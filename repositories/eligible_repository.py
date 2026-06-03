import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
file_path = DATA_DIR / "eligibles.json"


def get_all_eligible():
    with open(file_path) as f:
        return json.load(f)
    
def get_eligible(eligible_id):

    eligibles = get_all_eligible()
    for eligible in eligibles:
        if eligible["eligibleId"] == eligible_id:
                return eligible

    return None

def get_eligible_by_submission(submission_id):

    eligibles = get_all_eligible()
    eligibles_by_submission_id = []
    for eligible in eligibles:
        if eligible["submissionId"] == submission_id:
                eligibles_by_submission_id.append(eligible)

    return eligibles_by_submission_id


def get_eligible_by_customer(customer_id):

    eligibles = get_all_eligible()
    eligibles_by_customer_id = []
    for eligible in eligibles:
        if eligible["customerId"] == customer_id:
                eligibles_by_customer_id.append(eligible)

    return eligibles_by_customer_id

def get_eligible_by_offer(offer_id):

    eligibles = get_all_eligible()
    eligibles_by_offer_id = []
    for eligible in eligibles:
        if eligible["offerId"] == offer_id:
                eligibles_by_offer_id.append(eligible)

    return eligibles_by_offer_id


def is_submission_eligible(submission_id):

    eligibles = get_all_eligible()
    for eligible in eligibles:
        if eligible["submissionId"] == submission_id:
                return True

    return False
