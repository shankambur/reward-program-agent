# services/investigation_service.py

from repositories.submission_repository import get_submission,get_submissions_by_customer
from repositories.customer_repository import get_customer
from repositories.enrollment_repository import get_enrollments_by_customer,get_enrollments_by_offer
from repositories.offer_repository import get_offer
from repositories.eligible_repository import get_eligible_by_submission,get_eligible_by_offer
from repositories.credit_repository import get_credits_by_submission,get_credits_by_customer,get_credits_by_offer


def investigate_submission(submission_id):
    submission = get_submission(submission_id)

    if submission is None:
        return {
            "found": False,
            "message": f"No submission found for submissionId: {submission_id}"
        }

    customer_id = submission["customerId"]
    card_number = submission["cardNumber"]

    customer = get_customer(customer_id)

    all_customer_enrollments = get_enrollments_by_customer(customer_id)

    card_enrollments = []
    for enrollment in all_customer_enrollments:
        if enrollment["cardNumber"] == card_number:
            card_enrollments.append(enrollment)

    enrolled_offers = []
    for enrollment in card_enrollments:
        offer = get_offer(enrollment["offerId"])

        enrolled_offers.append({
            "enrollment": enrollment,
            "offer": offer
        })

    eligibles = get_eligible_by_submission(submission_id)
    credits = get_credits_by_submission(submission_id)

    return {
        "found": True,
        "submission": submission,
        "customer": customer,
        "enrolledOffers": enrolled_offers,
        "eligibles": eligibles,
        "credits": credits,
        "summary": {
            "submissionId": submission_id,
            "customerId": customer_id,
            "cardNumber": card_number,
            "transactionAmount": submission["transactionAmount"],
            "transactionDate": submission["transactionDate"],
            "enrollmentCountForCard": len(card_enrollments),
            "eligibleCount": len(eligibles),
            "creditCount": len(credits)
        }
    }


def investigate_customer(customer_id):
    customer = get_customer(customer_id)

    if customer is None:
        return {
            "found": False,
            "message": "Customer not found"
        }

    submissions = get_submissions_by_customer(customer_id)
    credits = get_credits_by_customer(customer_id)
    enrolled_offers = get_enrollments_by_customer(customer_id)

    return {
        "found": True,
        "customer": customer,
        "submissions": submissions,
        "credits": credits,
        "enrolledOffers": enrolled_offers
    }



def investigate_offer(offer_id):

    offer = get_offer(offer_id)

    if offer is None:
        return {
            "found": False,
            "message": "Offer not found"
        }

    enrollments = get_enrollments_by_offer(offer_id)
    eligibles = get_eligible_by_offer(offer_id)
    credits = get_credits_by_offer(offer_id)

    return {
        "found": True,
        "offer": offer,
        "enrollments": enrollments,
        "eligibles": eligibles,
        "credits": credits
    }