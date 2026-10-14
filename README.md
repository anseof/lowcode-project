# Flask Welcome Application

A minimal Flask 3.x web application contained in a single file (`app.py`). It features a simple form where users can enter their name, and upon submission, the form dynamically transitions to display a personalised welcome message along with a "Back" button.

## Project Files

`app.py`: The main Flask application containing the routing logic and embedded HTML/CSS template.

`requirements.txt`: Contains pinned project dependencies (`Flask>=3.0.0`).


---

## Installation & Setup

Open your terminal and navigate to your project directory.

2. Create a Python virtual environment:
```bash
   python -m venv .venv
```
   
3. Activate the virtual environment:
**On Windows (Command Prompt):**

```cmd
.venv\Scripts\activate

```


**On Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1

```


**On macOS / Linux:**

```bash
source .venv/bin/activate

```




4. Install the required dependencies:
```bash
pip install -r requirements.txt

```



---

## How to Run

Start the Flask development server:

```bash
python app.py

```


2. Open your web browser and go to the URL printed in your terminal (typically **http://127.0.0.1:5000**):
`http://127.0.0.1:5000`
3. Enter your name, click **Submit**, and enjoy your personalised welcome page!

```

```