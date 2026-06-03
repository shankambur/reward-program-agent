from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages, file_name,chunkSize,chunkOverlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunkSize,
        chunk_overlap=chunkOverlap
    )
    documents = []
    for page in pages:
        print("chunking")
        chunks = splitter.split_text(page["text"])
        chunkNumber = 0
        for chunk in chunks:
            print("each chunk")
            chunkNumber +=1
            print("__chunkNumber=",chunkNumber)
            documents.append(
                {
                    "content": chunk,
                    "source": file_name,
                    "page": page["page_number"]
                }
            )
    return documents