import pdfkit
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger
import os

# ✅ Set path to wkhtmltopdf manually
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

def read_urls(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_title(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "Untitled"
    except Exception:
        return None

def create_toc_html(titles_urls):
    toc_html = "<html><body><h1>Table of Contents</h1><ol>"
    for i, (title, url, status) in enumerate(titles_urls, 1):
        marker = "❌" if status == "dead" else ""
        display_title = title if title else "Untitled"
        toc_html += f"<li>{i}. {marker} {display_title}<br><small>{url}</small></li><br>"
    toc_html += "</ol></body></html>"
    toc_file = "toc.html"
    with open(toc_file, 'w', encoding='utf-8') as f:
        f.write(toc_html)
    return toc_file

def generate_pdf_from_urls(url_file, output_pdf):
    urls = read_urls(url_file)
    titles_urls = []
    temp_pdfs = []

    with open("error_log.txt", "w", encoding="utf-8") as log:
        for i, url in enumerate(urls, 1):
            title = get_title(url)
            if title is None:
                log.write(f"[{i}] DEAD LINK: {url}\n")
                titles_urls.append(("Untitled", url, "dead"))
                continue

            titles_urls.append((title, url, "live"))
            pdf_file = f"page_{i}.pdf"
            try:
                print(f"📄 Converting: {url} → {pdf_file}")
                pdfkit.from_url(url, pdf_file, configuration=config)
                temp_pdfs.append(pdf_file)
            except Exception as e:
                log.write(f"[{i}] ERROR converting {url}: {str(e)}\n")
                titles_urls[-1] = (title, url, "dead")

    toc_html = create_toc_html(titles_urls)
    pdfkit.from_file(toc_html, "toc.pdf", configuration=config)
    temp_pdfs.insert(0, "toc.pdf")

    merger = PdfMerger()
    for pdf in temp_pdfs:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()

    for f in temp_pdfs + ["toc.html"]:
        os.remove(f)

    print(f"\n✅ PDF created: {output_pdf}")
    print("📄 Error log saved to: error_log.txt")

generate_pdf_from_urls("urls.txt", "combined_webpages_with_toc.pdf")
