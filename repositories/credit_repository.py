import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
file_path = DATA_DIR / "credits.json"

def get_all_credits():
    with open(file_path) as f:
        return json.load(f)
    
def get_credit(credit_id):

    credits = get_all_credits()
    for credit in credits:
        if credit["creditId"] == credit_id:
                return credit

    return None

def get_credits_by_submission(submission_id):

    credits = get_all_credits()
    credits_by_submission_id = []
    for credit in credits:
        if credit["submissionId"] == submission_id:
                credits_by_submission_id.append(credit)

    return credits_by_submission_id


def get_credits_by_customer(customer_id):

    credits = get_all_credits()
    credits_by_customer_id = []
    for credit in credits:
        if credit["customerId"] == customer_id:
                credits_by_customer_id.append(credit)

    return credits_by_customer_id

def get_credits_by_offer(offer_id):

    credits = get_all_credits()
    credits_by_offer_id = []
    for credit in credits:
        if credit["offerId"] == offer_id:
                credits_by_offer_id.append(credit)

    return credits_by_offer_id

def get_credits_by_eligible(eligible_id):

    credits = get_all_credits()
    credits_by_eligible = []
    for credit in credits:
        if credit["eligibleId"] == eligible_id:
                credits_by_eligible.append(credit)

    return credits_by_eligible


def get_credits_by_status(credit_status):

    credits = get_all_credits()
    credits_by_status = []
    for credit in credits:
        if credit["creditStatus"] == credit_status:
                credits_by_status.append(credit)

    return credits_by_status

def get_credits_by_card_number(card_number):

    credits = get_all_credits()
    credits_by_card_number = []
    for credit in credits:
        if credit["cardNumber"] == card_number:
                credits_by_card_number.append(credit)

    return credits_by_card_number