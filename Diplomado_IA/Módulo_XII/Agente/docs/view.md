# view/view.py

Description
-----------
Simple Gradio frontend that connects to the `AgentGPT2` agent. It provides
chat functionality with a `Chatbot`, a `Textbox` for user input, a "Send"
button, and a button to clear the conversation.

Source file: view/view.py

Public functions
----------------
- `chat(message, history)`:
  - Description: Sends `message` to the agent, appends the user's message
    and the assistant's response to `history`, and returns a tuple
    suitable for Gradio callbacks: `("", history)`.
  - Parameters:
    - `message` (str): text entered by the user.
    - `history` (list[dict]): conversation history as a list of dictionaries
      with `role` and `content` keys.
  - Returns: `(new_input_value, updated_history)` — `new_input_value` is an
    empty string to clear the textbox.

- `launch()`:
  - Description: Launches the Gradio server (`demo.launch()`).
  - Usage: Blocks while the server is running.

Usage
-----
From Python:

```python
from view.view import launch

launch()
```

Requirements
------------
- `gradio` installed (version compatible with `Blocks` and `Chatbot`).
- `AgentGPT2` implemented in `agent/AgentGPT2.py` and importable.

Notes
-----
- The UI text and labels are in Spanish (course project).
- `chat` expects the `history` format used by Gradio `Chatbot`.

Run locally
-----------
Install dependencies and run the main script or import `launch()`:

```bash
pip install -r requirements.txt
python main.py
```

(Or run from a module that imports `launch()`.)
