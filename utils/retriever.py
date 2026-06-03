def retrieve_chunks(vector_store, question, top_k, score_threshold, pdf_filter):
    search_filter = None

    if pdf_filter != "All Documents":
        search_filter = {
            "source": pdf_filter
        }

    results = vector_store.similarity_search_with_score(
        question,
        k=top_k,
        filter=search_filter
    )

    filtered_results = [
        (doc, score)
        for doc, score in results
        if score <= score_threshold
    ]

    return filtered_results,len(results)