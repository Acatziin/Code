# main.py

Description
-----------
Minimal entrypoint that starts the Gradio interface defined in
`view/view.py`. It is intended to run the application locally with
`python main.py` or to be imported from other modules without automatically
starting the server.

Relevant contents
-----------------
- `main()` — function that calls `view.view.launch()` to start the
  Gradio server.
- `if __name__ == "__main__": main()` — allows running the module as a
  script or importing the `main` function without executing the application.

Usage
-----
Run locally:

```bash
python main.py
```

Call from Python:

```python
from main import main
main()
```

Requirements
------------
- Install the dependencies listed in `requirements.txt` (e.g.
  `gradio`, `transformers`, `torch`).

Notes
-----
- The Gradio server will print a local URL in the console to access the
  interface.
- For automated tests or import into other modules, import `main` instead of
  running the script directly.

Quick start
-----------
Install dependencies and run:

```bash
pip install -r requirements.txt
python main.py
```

The interface will open in the browser or show a local URL in the console.

