# TestVerse-SuperAgent

A desktop “SuperAgent” for automating browser-based QA flows with a business-risk mindset. All core logic is compiled into native extensions (`.pyd`), so your source code stays hidden. You ship only:

- `main.cp311-win_amd64.pyd`
- `logic.cp311-win_amd64.pyd`
- `cli.cp311-win_amd64.pyd`
- `start.py`
- `ui.qss`

---

## 🚀 Prerequisites

- **Windows 10/11**, 64-bit  
- **Python 3.11** installed and on `PATH`  
- **Playwright** browsers installed (only on first run; the app will auto-download Chromium):

  ```powershell
  pip install playwright
  python -m playwright install chromium
  ```

- **PySide6** (Qt for Python):

  ```powershell
  pip install PySide6
  ```

---

## 📦 Installation

1. **Clone or download** this repo to your machine.  
2. **Create a virtual environment** (recommended):

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Qt & Playwright** (if you haven’t already):

   ```powershell
   pip install PySide6 playwright
   python -m playwright install chromium
   ```

*(No need to install your own copies of the compiled modules — they’re already here.)*

---

## ▶️ Usage

From the project root (with your venv activated):

```powershell
python start.py
```

That will:

1. Launch the TestVerse SuperAgent GUI.  
2. Download Chromium (on first run) into a private folder.  
3. Drive your QA flows, logging each step and generating a professional summary when done.

---

## ⚙️ Command-Line Mode

If you need a terminal interface instead of the GUI:

```powershell
python -c "import cli; cli.main()"
```

*(Requires the same prerequisites above.)*

---


