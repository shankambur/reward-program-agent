from services.investigation_service import (
    investigate_submission,
    investigate_customer,
    investigate_offer
)

def get_app_settings(settings, include_advanced=False):
    print("Executing get_app_settings")

    result = {
        "top_k": settings.get("top_k"),
        "score_threshold": settings.get("score_threshold"),
        "memory_count": settings.get("memory_count"),
        "temperature": settings.get("temperature"),
        "show_debug": settings.get("show_debug"),
    }

    if include_advanced:
        result["chunk_size"] = settings.get("chunk_size")
        result["chunk_overlap"] = settings.get("chunk_overlap")
        result["rerank_top_n"] = settings.get("rerank_top_n")
        result["pdf_filter"] = settings.get("pdf_filter")

    return result

def get_document_count(pdf_sources):
    print("Executing get_document_count")

    if not pdf_sources:
        return 0

    return len(pdf_sources)

def get_loaded_documents(pdf_sources):
    print("Executing get_loaded_documents")

    if not pdf_sources:
        return []

    return [fileName for fileName in pdf_sources]


def investigate_submission_tool(submission_id):
    return investigate_submission(submission_id)

def investigate_customer_tool(customer_id):
    return investigate_customer(customer_id)

def investigate_offer_tool(offer_id):
    return investigate_offer(offer_id)