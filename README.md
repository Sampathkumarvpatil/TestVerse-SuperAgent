# TestVerse SuperAgent

**TestVerse SuperAgent** is a desktop tool that automates common browser-based QA workflows through a simple GUI or command-line interface.

---

## 🚀 Quick Start (GUI)

1. **Clone** or **Download ZIP** of this repository.
2. **Install Python 3.11** (or later) from [python.org](https://python.org) and make sure it's on your system `PATH`.
3. Open a terminal in the project folder and create a virtual environment (optional but recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```powershell
   pip install PySide6 playwright
   python -m playwright install chromium
   ```
5. **Run the application**:
   ```powershell
   python start.py
   ```

The GUI window will appear. Enter your test instructions in the prompt area and click **Run Test**.

---

## ⚙️ Command-Line Mode

If you prefer a terminal interface, run:

```powershell
python -c "import cli; cli.main()"
```

Follow on-screen prompts to input your steps one by one.

---

## 📄 Files Included

- `start.py` — launcher for the GUI
- `cli.cp311-win_amd64.pyd` — compiled command-line logic
- `logic.cp311-win_amd64.pyd` — compiled core engine
- `main.cp311-win_amd64.pyd` — compiled GUI window
- `ui.qss` — styling for the GUI

> **Note:** You do not need to edit or view the compiled modules.

---

## 📝 How It Works

- **GUI Mode**: Provides a terminal-like interface with run/stop controls.
- **CLI Mode**: Step-by-step input via the console.
- Under the hood, the tool executes your browser automation steps and logs each action.

---

## 🛠 Support

If you encounter issues:

- Ensure your Python environment is active and on `PATH`.
- Verify that Playwright installed Chromium correctly.
- Check for any error messages in the terminal output.

For further help, open an issue on this GitHub repository.

