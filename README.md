# MarkItDown Batch Converter 📝🔄

A powerful, user-friendly batch file converter built with Streamlit that transforms various document formats into clean Markdown. Powered by Microsoft's `markitdown` library.

🔗 **Live App:** [Deploy on Streamlit](https://markitdown-batch-converter.streamlit.app/)

---

## ✨ Features

- **Batch Conversion:** Upload and convert multiple files simultaneously.
- **Wide Format Support:** Converts PDF, DOCX, XLSX, PPTX, HTML, Images (JPG, PNG), and audio files to Markdown.
- **Instant Previews:** View converted Markdown text directly in your browser.
- **Easy Download:** Download converted files individually or together as a single ZIP archive.
- **Clean UI:** Simple drag-and-drop interface.

---

## 🛠️ Installation & Local Setup

If you want to run this application locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/sazidshahjada/markitdown-batch-converter.git
cd markitdown-batch-converter
```

### 2. Create a Virtual Environment
```bash
python3 -m venv markitdown_env
source markitdown_env/bin/activate  # On linux
markitdown_env\Scripts\activate  # On windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📦 Dependencies

The application relies on the following main Python libraries:
- `streamlit` - For the web interface framework.
- `markitdown` - For Microsoft's document-to-markdown conversion engine.

---

## 🚀 Deployment

This app is configured for instant deployment on **Streamlit Community Cloud**. 

When deploying, ensure your GitHub repository contains:
1. `app.py` (The main application entry point)
2. `requirements.txt` (Listing all necessary packages)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
