from services.investigation_service import (
    investigate_submission,
    investigate_customer,
    investigate_offer
)

def investigate_submission_tool(submission_id):
    return investigate_submission(submission_id)

def investigate_customer_tool(customer_id):
    return investigate_customer(customer_id)

def investigate_offer_tool(offer_id):
    return investigate_offer(offer_id)