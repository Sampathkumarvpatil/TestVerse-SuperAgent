# TestVerse SuperAgent

**TestVerse SuperAgent** is a desktop tool that automates browser-based QA workflows via a simple GUI or command-line interface.

---

## 🚀 Quick Start (GUI)

1. **Clone** or **Download ZIP** of this repository.
2. **Install Python 3.11** (or later) from [python.org](https://python.org) and ensure it's on your system `PATH`.
3. Open a terminal in the project folder and create a virtual environment (recommended):
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
6. **Obtain your API Key** by contacting Dr. Sanjeev Kuwadekar (sanjk0604@gmail.com) or Dr. Sampath V. Patil (drsampathkumarpatil@gmail.com). After you receive your key, launch the app, click the gear icon (⚙️) in the top‑right, and paste it under **Settings**.

Open the window, enter your test instructions in the prompt area and click **Run Test**.

---


## 📄 Files Included

- `start.py` — launcher for the GUI
- `cli.cp311-win_amd64.pyd` — compiled command-line logic
- `logic.cp311-win_amd64.pyd` — compiled core engine
- `main.cp311-win_amd64.pyd` — compiled GUI window
- `ui.qss` — styling for the GUI

> 📌 You do not need to edit or view the compiled modules.

---

## 📝 Configuration

After obtaining your API key (see above), click the ⚙️ icon at the top‑right to paste it into the Settings dialog. The app requires this key to connect to the AI service. For getting api key ,contact us.

---

## 🛠 Support & Contact

If you run into issues or need help, contact:

- Dr. Sanjeev Kuwadekar: sanjk0604@gmail.com
- Dr. Sampath V. Patil: drsampathkumarpatil@gmail.com

Or open an issue on this GitHub repository.

---

## 🗓 Version & Licensing

Released under the MIT License. See [LICENSE](LICENSE) for details.

