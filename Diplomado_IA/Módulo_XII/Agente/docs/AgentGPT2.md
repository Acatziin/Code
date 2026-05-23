# agent/AgentGPT2.py

Description
-----------
`AgentGPT2` is a lightweight wrapper around a GPT-2 model (Hugging Face
Transformers) that maintains a short conversation history and generates
assistant responses. It is intended for demonstration and educational use.

Class summary
-------------
- `AgentGPT2(model='gpt2', max_history=4)`:
  - Initializes the tokenizer and model with `from_pretrained(modelo)`.
  - Sets `pad_token` to the tokenizer's `eos_token`.
  - `max_history` controls how many turns are stored in `history`.

Public methods
--------------
- `build_prompt(user_message: str) -> str`:
  - Builds the prompt to send to the model. It includes a short initial
    instruction, the conversation history, and the user's message, leaving
    the assistant response position open.

- `answer(user_message: str) -> str`:
  - Generates the assistant response using `model.generate` with sampling.
    Decodes the output and extracts the text corresponding to the
    assistant's reply.
  - Appends the `(user_message, assistant_reply)` pair to `history` and
    trims the history if it exceeds `max_history`.

Important generation parameters
-----------------------------
- `max_new_tokens=80`
- `do_sample=True`, `temperature=0.7`
- `top_k=50`, `top_p=0.95`
- `repetition_penalty=1.2`

Requirements
------------
- `transformers`
- `torch`

Usage example
-------------
```python
from agent.AgentGPT2 import AgentGPT2

agent = AgentGPT2(modelo='gpt2', max_history=4)
reply = agent.answer('Hello, how are you?')
print(reply)
```

Notes
-----
- The prompt and response extraction are simple; for production use, it is
  recommended to prepare more robust prompts and handle tokenization/
  truncation more carefully.
- The default `gpt2` model is small and may not provide coherent responses
  in complex dialogues.
