# Import the necessary library
import weasyprint

def html_to_pdf(input_html_path, output_pdf_path):
    """
    Convert an HTML file with inline CSS to a PDF.
    
    :param input_html_path: Path to the input HTML file.
    :param output_pdf_path: Path to save the generated PDF file.
    """
    try:
        # Read the HTML file
        with open(input_html_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()

        # Use WeasyPrint to convert the HTML to PDF
        weasyprint.HTML(string=html_content).write_pdf(output_pdf_path)

        print(f"PDF successfully created: {output_pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_html = "input.html"  # Path to your input HTML file with inline CSS
    output_pdf = "output.pdf"  # Path to save the output PDF file
    
    html_to_pdf(input_html, output_pdf)
