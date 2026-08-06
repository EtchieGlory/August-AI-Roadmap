from pypdf import PdfReader


def count_pages():
    try:
        file_name = input("Enter PDF filename: ").strip()

        if not file_name.lower().endswith(".pdf"):
            file_name += ".pdf"

        reader = PdfReader(f"pdfs/{file_name}")

        print(f"\nNumber of pages: {len(reader.pages)}")

    except FileNotFoundError:
        print("❌ File not found.")

    pause()
    
    

def extract_text():
    try:
        file_name = input("Enter PDF filename: ").strip()

        if not file_name.lower().endswith(".pdf"):
            file_name += ".pdf"

        reader = PdfReader(f"pdfs/{file_name}")

        for number, page in enumerate(reader.pages, start=1):
            print(f"\n{'=' * 30} Page {number} {'=' * 30}")

            text = page.extract_text()

            if text:
                print(text)
            else:
                print(f"No text found on page {number}.")

    except FileNotFoundError:
        print("❌ File not found.")

    pause()
    
    

def merge_pdfs():
    try:
        merger = PdfWriter()

        total = int(input("How many PDFs do you want to merge? "))

        for i in range(total):
            file_name = input(f"Enter PDF {i + 1}: ").strip()

            if not file_name.lower().endswith(".pdf"):
                file_name += ".pdf"

            reader = PdfReader(f"pdfs/{file_name}")

            for page in reader.pages:
                merger.add_page(page)

        output_name = input("Output filename: ").strip()

        if not output_name.lower().endswith(".pdf"):
            output_name += ".pdf"

        with open(f"output/{output_name}", "wb") as output:
            merger.write(output)

        print("\n✅ PDFs merged successfully!")

    except FileNotFoundError:
        print("❌ One or more PDF files were not found.")

    pause()
    
    

def split_pdf():
    try:
        file_name = input("Enter PDF filename: ").strip()

        if not file_name.lower().endswith(".pdf"):
            file_name += ".pdf"

        reader = PdfReader(f"pdfs/{file_name}")

        for number, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()

            writer.add_page(page)

            with open(f"output/{file_name.rsplit('.', 1)[0]}_{number}.pdf", "wb") as output:
                writer.write(output)

        print("\n✅ PDF split successfully!")

    except FileNotFoundError:
        print("❌ File not found.")

    pause()

def display_menu():
    print(f"""
{'=' * 30} PDF TOOLKIT {'=' * 30}

1. Count Pages
2. Extract Text
3. Merge PDFs
4. Split PDF
5. Exit
""")
def pause():
    input("\nPress Enter to continue...")
    
while True:
   display_menu()
   
   choice = input('Choose (1-5): ').strip()
   
   if choice == "1":
      count_pages()

   elif choice == "2":
      extract_text()

   elif choice == "3":
      merge_pdfs()

   elif choice == "4":
      split_pdf()

   elif choice == "5":
      print('Goodbye!')
      break
   else:
    print("Invalid choice. Please try again.")