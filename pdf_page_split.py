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

        # Prompt the user for the number of pages before creating a new file
        num_pages_per_file = int(input("Enter the number of pages before a new file: "))

        # Append timestamp to the output directory name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_dir = os.path.join(os.path.dirname(file_path), f'split_files_{timestamp}')
        os.makedirs(output_dir, exist_ok=True)

        # Iterate over each page and save it as a separate file
        for page_number in range(0, total_pages, num_pages_per_file):
            writer = PdfWriter()
            for offset in range(num_pages_per_file):
                current_page = page_number + offset
                if current_page >= total_pages:
                    break
                page = pdf.pages[current_page]
                writer.add_page(page)

            output_filename = os.path.join(output_dir, f'pages_{page_number + 1}_to_{min(page_number + num_pages_per_file, total_pages)}.pdf')

            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)

            print(f"Pages {page_number + 1} to {min(page_number + num_pages_per_file, total_pages)} saved as {output_filename}")

# Usage
split_pdf()
