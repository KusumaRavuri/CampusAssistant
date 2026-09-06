import fitz
import os

# -----------------------------
# 1. Folders
# -----------------------------

documents_folder = "documents"
output_path = "backend/regulations.txt"

# -----------------------------
# 2. Find all PDF files
# -----------------------------

pdf_files = [
    file
    for file in os.listdir(documents_folder)
    if file.lower().endswith(".pdf")
]

if not pdf_files:
    raise FileNotFoundError(
        "No PDF files found in the documents folder."
    )

print(f"Found {len(pdf_files)} PDF files.")

# -----------------------------
# 3. Extract text from all PDFs
# -----------------------------

with open(output_path, "w", encoding="utf-8") as output_file:

    for pdf_file in pdf_files:

        pdf_path = os.path.join(documents_folder, pdf_file)

        print(f"\nProcessing: {pdf_file}")

        doc = fitz.open(pdf_path)

        # Store document name
        output_file.write("\n\n")
        output_file.write("=" * 80 + "\n")
        output_file.write(f"DOCUMENT: {pdf_file}\n")
        output_file.write("=" * 80 + "\n")

        # Extract every page
        for page_number, page in enumerate(doc):

            text = page.get_text()

            output_file.write(
                f"\n--- Page {page_number + 1} ---\n"
            )

            output_file.write(text)

        doc.close()

        print(f"Completed: {pdf_file}")

# -----------------------------
# 4. Finished
# -----------------------------

print("\n================================")
print("PDF TEXT EXTRACTION COMPLETED")
print("================================")
print(f"Total PDFs processed: {len(pdf_files)}")
print(f"Text saved to: {output_path}")