import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog
from datetime import datetime

def split_pdf():
    # Prompt the user to select the PDF file
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    root.destroy()

    if not file_path:
        print("No file selected. Exiting.")
        return

    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        total_pages = len(pdf.pages)

        # Append timestamp to the output directory name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_dir = os.path.join(os.path.dirname(file_path), f'split_files_{timestamp}')
        os.makedirs(output_dir, exist_ok=True)

        # Iterate over each page and save it as a separate file
        for page_number in range(total_pages):
            page = pdf.pages[page_number]
            output_filename = os.path.join(output_dir, f'page_{page_number + 1}.pdf')

            writer = PdfWriter()
            writer.add_page(page)

            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)

            print(f"Page {page_number + 1} saved as {output_filename}")

# Usage
split_pdf()
