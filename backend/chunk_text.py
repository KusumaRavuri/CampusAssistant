import re
import json

input_path = "backend/regulations.txt"
output_path = "backend/chunks.json"

# -----------------------------
# 1. Read extracted text
# -----------------------------

with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()

chunks = []

# -----------------------------
# 2. Find each document
# -----------------------------

document_pattern = re.compile(
    r"DOCUMENT:\s*(.+?)\n\s*(?=--- Page \d+ ---)",
    re.DOTALL
)

documents = document_pattern.finditer(text)

# -----------------------------
# 3. Process each document
# -----------------------------

for document_match in documents:

    source = document_match.group(1).strip()

    # Start from the first page after the document name
    document_start = document_match.end()

    # Find where the next document starts
    next_document = re.search(
        r"\n={80}\s*\nDOCUMENT:",
        text[document_start:]
    )

    if next_document:
        document_text = text[
            document_start:
            document_start + next_document.start()
        ]
    else:
        document_text = text[document_start:]

    # -----------------------------
    # 4. Split document into pages
    # -----------------------------

    pages = re.split(
        r"--- Page (\d+) ---",
        document_text
    )

    # pages:
    # [text_before_page, page_number, page_text, ...]

    for i in range(1, len(pages), 2):

        page_number = int(pages[i])
        page_text = pages[i + 1].strip()

        # Skip completely empty pages
        if not page_text:
            continue

        # -----------------------------
        # 5. Clean whitespace
        # -----------------------------

        page_text = re.sub(r"\s+", " ", page_text).strip()

        words = page_text.split()

        # -----------------------------
        # 6. Create overlapping chunks
        # -----------------------------

        chunk_size = 150
        overlap = 30

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            if chunk_text.strip():

                chunks.append({
                    "text": chunk_text,
                    "page": page_number,
                    "source": source
                })

            # Move forward while maintaining overlap
            start += chunk_size - overlap

# -----------------------------
# 7. Save chunks
# -----------------------------

with open(output_path, "w", encoding="utf-8") as file:

    json.dump(
        chunks,
        file,
        indent=2,
        ensure_ascii=False
    )

# -----------------------------
# 8. Print result
# -----------------------------

print("================================")
print("CHUNKING COMPLETED")
print("================================")
print(f"Total chunks: {len(chunks)}")
print(f"Chunks saved to: {output_path}")