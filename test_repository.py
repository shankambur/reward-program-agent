from repositories import customer_repository, offer_repository, enrollment_repository,submission_repository,eligible_repository,credit_repository

print("**** Test Repository for Customer **** \n")
print("Customer:get_customer")
print(customer_repository.get_customer("C1001"))

print("\nCustomer:get_customer")
print(customer_repository.get_customer("C2002"))

print("\nCustomer:get_customer")
print(customer_repository.get_customer("C2002"))

print("\nCustomer:get_customer")
print(customer_repository.get_customer("C9009"))

print("\nCustomer Count:get_all_customers")
print(len(customer_repository.get_all_customers()))

print("\n**** Test Repository for Offer **** \n")
print("\nOffer:get_offer")
print(offer_repository.get_offer("OFF400"))

print("\nOffer:get_offer")
print(offer_repository.get_offer("OFF700"))

print("\nOffer:get_offer")
print(offer_repository.get_offer("OFF900"))

print("\nOffer Count:get_all_offers")
print(len(offer_repository.get_all_offers()))


print("\n**** Test Repository for Enrollment **** \n")
print("\nEnrollment Count:get_all_enrollments")
print(len(enrollment_repository.get_all_enrollments()))

print("\nEnrollment:get_enrollments_by_customer")
print(enrollment_repository.get_enrollments_by_customer("C1009"))

print("\nEnrollment:get_enrollments_by_offer")
print(enrollment_repository.get_enrollments_by_offer("OFF900"))

print("\nEnrollment:get_enrollments_by_customer")
print(enrollment_repository.get_enrollments_by_customer("C1004"))

print("\nEnrollment:get_enrollments_by_offer")
print(enrollment_repository.get_enrollments_by_offer("OFF800"))

print("\nEnrollment:is_customer_enrolled")
print(enrollment_repository.is_customer_enrolled("C9009","OFF900"))


print("\n**** Test Repository for Submission **** \n")
print("Submission Count:get_all_submissions")
print(len(submission_repository.get_all_submissions()))

print("\nSubmission:get_submission:SUB0003")
print(submission_repository.get_submission("SUB0003"))

print("\nSubmission:get_submission:SUB9999")
print(submission_repository.get_submission("SUB9999"))

print("\nSubmission:get_submissions_by_customer:C1002")
print(submission_repository.get_submissions_by_customer("C1002"))

print("\nSubmission:get_submissions_by_customer:C9999")
print(submission_repository.get_submissions_by_customer("C9999"))

print("\nSubmission:get_submissions_by_cardNumber:371449635399004")
print(submission_repository.get_submissions_by_card_number("371449635399004"))

print("\nSubmission:get_submissions_by_cardNumber:991449635399004")
print(submission_repository.get_submissions_by_card_number("991449635399004"))


print("\n**** Test Repository for Eligible **** \n")
print("Eligible Count:get_all_eligible")
print(len(eligible_repository.get_all_eligible()))

print("\nEligible:get_eligible:ELG0001")
print(eligible_repository.get_eligible("ELG0001"))

print("\nEligible:get_eligible:ELG9999")
print(eligible_repository.get_eligible("ELG9999"))

print("\nEligible:get_eligible_by_customer:C1001")
print(eligible_repository.get_eligible_by_customer("C1001"))

print("\nEligible:get_eligible_by_customer:C9999")
print(eligible_repository.get_eligible_by_customer("C9999"))

print("\nEligible:get_eligible_by_offer:OFF400")
print(eligible_repository.get_eligible_by_offer("OFF400"))

print("\nEligible:get_eligible_by_offer:OFF999")
print(eligible_repository.get_eligible_by_offer("OFF999"))

print("\nEligible:get_eligible_by_submission:SUB0001")
print(eligible_repository.get_eligible_by_submission("SUB0001"))

print("\nEligible:get_eligible_by_submission:SUB9999")
print(eligible_repository.get_eligible_by_submission("SUB9999"))

print("\nEligible:is_submission_eligible:SUB0007")
print(eligible_repository.is_submission_eligible("SUB0007"))

print("\nEligible:is_submission_eligible:SUB9999")
print(eligible_repository.is_submission_eligible("SUB9999"))


print("\n**** Test Repository for Credits **** \n")
print("Credits Count:get_all_credits")
print(len(credit_repository.get_all_credits()))

print("\nCredits:get_credit:CR0001")
print(credit_repository.get_credit("CR0001"))

print("\nCredits:get_credit:CR9999")
print(credit_repository.get_credit("CR9999"))

print("\nCredits:get_credits_by_card_number:371449635399001")
print(credit_repository.get_credits_by_card_number("371449635399001"))

print("\nCredits:get_credits_by_card_number:971449635399001")
print(credit_repository.get_credits_by_card_number("971449635399001"))

print("\nCredits:get_credits_by_customer:C1004")
print(credit_repository.get_credits_by_customer("C1004"))

print("\nCredits:get_credits_by_customer:C9999")
print(credit_repository.get_credits_by_customer("C9999"))

print("\nCredits:get_credits_by_eligible:ELG0007")
print(credit_repository.get_credits_by_eligible("ELG0007"))

print("\nCredits:get_credits_by_eligible:ELG9999")
print(credit_repository.get_credits_by_eligible("ELG9999"))

print("\nCredits:get_credits_by_offer:OFF800")
print(credit_repository.get_credits_by_offer("OFF800"))

print("\nCredits:get_credits_by_offer:OFF999")
print(credit_repository.get_credits_by_offer("OFF999"))

print("\nCredits:get_credits_by_status:ISSUED")
print(credit_repository.get_credits_by_status("ISSUED"))

print("\nCredits:get_credits_by_status:SUCCESS")
print(credit_repository.get_credits_by_status("SUCCESS"))

print("\nCredits:get_credits_by_submission:SUB0007")
print(credit_repository.get_credits_by_submission("SUB0007"))

print("\nCredits:get_credits_by_submission:SUB9999")
print(credit_repository.get_credits_by_submission("SUB9999"))