"""Simple Gradio frontend for the AgentGPT2 chatbot.

This module exposes a Gradio Blocks UI that connects to the
`AgentGPT2` agent implementation. It provides a small chat
interface with a textbox, send button and a clear conversation
button. The main entrypoint for programmatic use is `launch()`.

The UI text and messages are written in Spanish since this project
is part of a Spanish-language course.

Example:
    from view.view import launch
    launch()

Functions
---------
chat(message, history)
    Handle a single chat turn: send `message` to the agent, append
    both user and assistant messages to `history` and return the
    updated chat state suitable for Gradio callbacks.

launch()
    Start the Gradio demo server (calls `demo.launch()`).
"""

from agent.AgentGPT2 import AgentGPT2
import gradio as gr
from typing import List, Dict, Tuple

agent = AgentGPT2()

def chat(message: str, history: List[Dict[str, str]]) -> Tuple[str, List[Dict[str, str]]]:
    """Process a user message and update the chat history.

    Parameters
    - message: The user's input text.
    - history: The conversation history as a list of dicts with
      keys `role` and `content`. This follows Gradio's chat widget
      convention.

    Returns
    A tuple of ``(new_input_value, updated_history)`` where
    `new_input_value` is an empty string (to clear the textbox)
    and `updated_history` is the modified history including the
    user's message and the agent's response.
    """

    answer = agent.answer(message)

    history.append((message, answer))

    return "", history



with gr.Blocks(title="Chatbot con GPT-2") as demo:

    gr.Markdown("# Chatbot inteligente usando GPT-2")
    gr.Markdown("Práctica del diplomado en Inteligencia Artificial")

    chatbot = gr.Chatbot(
        label="Conversación"
    )

    message = gr.Textbox(
        label="Escribe tu mensaje",
        placeholder="Pregunta algo al agente..."
    )

    send = gr.Button("Enviar")
    clean = gr.Button("Limpiar conversación")

    send.click(
        chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    message.submit(
        chat,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )

    clean.click(
        lambda: [],
        outputs=chatbot
    )
    

def launch() -> None:
    """Launch the Gradio demo server for the chatbot.

    This function blocks while the Gradio server is running.
    """

    demo.launch(share=True) # To get a public URL for testing on mobile or sharing with others. Remove `share=True` for local-only access.