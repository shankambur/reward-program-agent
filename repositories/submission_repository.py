import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
file_path = DATA_DIR / "submissions.json"

def get_all_submissions():
    with open(file_path) as f:
        return json.load(f)
    

def get_submission(submission_id):

    submissions = get_all_submissions()
    for submission in submissions:
        if submission["submissionId"] == submission_id:
                return submission

    return None

def get_submissions_by_customer(customer_id):

    submissions = get_all_submissions()
    submissions_by_customer = []
    for submission in submissions:
        if submission["customerId"] == customer_id:
                submissions_by_customer.append(submission)

    return submissions_by_customer

def get_submissions_by_card_number(card_number):

    submissions = get_all_submissions()
    submissions_by_cardNumber = []
    for submission in submissions:
        if submission["cardNumber"] == card_number:
                submissions_by_cardNumber.append(submission)

    return submissions_by_cardNumber

