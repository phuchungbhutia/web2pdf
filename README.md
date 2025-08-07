<<<<<<< HEAD
# web2pdf
Web2PDF: Convert URLs to PDF with Dead Link Handling  Effortlessly convert a list of webpage URLs into a single, well-organized PDF. Includes automatic dead link detection, logging, and a dynamic Table of Contents.
=======
# 🧾 Web2PDF: Convert URLs to PDF with Dead Link Handling

Effortlessly convert a list of webpage URLs into a single, well-organized PDF. Includes automatic dead link detection, logging, and a dynamic Table of Contents.

![GitHub Repo Size](https://img.shields.io/github/repo-size/phuchungbhutia/web2pdf)
![GitHub Stars](https://img.shields.io/github/stars/phuchungbhutia/web2pdf?style=social)
![GitHub Forks](https://img.shields.io/github/forks/phuchungbhutia/web2pdf?style=social)
![MIT License](https://img.shields.io/github/license/phuchungbhutia/web2pdf)

---

## 📦 Features

- ✅ Skips unreachable URLs without crashing
- 📝 Logs dead links to `error_log.txt`
- 📄 Adds dead links to TOC with ❌ marker
- 📚 Generates a clean, merged PDF
- 🧠 Uses `pdfkit`, `PyPDF2`, `BeautifulSoup`, and `requests`
- 🧾 Modular and easy to extend

---

## 🔗 Extracting Links with Chrome Extension

Use the [List All Links Chrome Extension](https://chromewebstore.google.com/detail/list-all-links/kmdahcegpgbgcpadeomdieodglfedabj?hl=en-US&utm_source=ext_sidebar) to extract all links from a webpage:

1. Install the extension
2. Right-click on any webpage → “List all links”
3. Copy the links and paste them into `urls.txt` (one per line)

---

## 🛠️ Installation Guide

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install `wkhtmltopdf`

- Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
- Install to: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`

### 3. Fix Path Issues (Windows)

#### ✅ Add Python to PATH

```cmd
setx PATH "%PATH%;C:\Python311\;C:\Python311\Scripts\"
```

> Replace with your actual Python path.

#### ✅ Add wkhtmltopdf to PATH

```cmd
setx PATH "%PATH%;C:\Program Files\wkhtmltopdf\bin\"
```

#### ✅ Manual Path in Script

If needed, set path manually in `generate_pdf.py`:

```python
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
```

---

## 📂 Folder Structure

```
web2pdf/
├── generate_pdf.py         # Main script
├── urls.txt                # List of webpage URLs
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Ignore temp files
├── requirements.txt        # Python dependencies
```

---

## 📄 Usage Instructions

1. Add your URLs to `urls.txt` (one per line)
2. Run the script:

```bash
python generate_pdf.py
```

3. Output:
   - `combined_webpages_with_toc.pdf`
   - `error_log.txt`

---

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=phuchungbhutia&layout=compact&theme=radical)

---

## 🔄 GitHub Setup & Update Commands

```bash
git init
git remote add origin https://github.com/phuchungbhutia/web2pdf.git
git add .
git commit -m "Initial commit with PDF generator and setup"
git branch -M main
git push -u origin main
```

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 📬 Contact

For questions or collaborations, reach out via [GitHub Issues](https://github.com/phuchungbhutia/web2pdf/issues).
>>>>>>> ceab38b (Initial commit with PDF generator and setup)
