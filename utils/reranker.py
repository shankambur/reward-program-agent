def limit_context_chunks(results_with_score, rerank_top_n):
    sorted_results = sorted(
        results_with_score,
        key=lambda item: item[1]
    )

    return sorted_results[:rerank_top_n]