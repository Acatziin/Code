"""AgentGPT2

Lightweight wrapper around a GPT-2 model (Hugging Face Transformers)
that maintains a short conversation history and generates assistant
responses. Designed for educational/demonstration usage in the
course project.

The class keeps a `history` of (user, assistant) pairs and constructs
a simple prompt that is passed to the GPT-2 language model to produce
the next assistant reply.
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from typing import List, Tuple


class AgentGPT2:
    """GPT-2 based conversational agent.

    Parameters
    - model: model identifier compatible with `from_pretrained` (default: "gpt2").
    - max_history: maximum number of (user, assistant) turns to keep in history.
    """

    def __init__(self, model: str = "gpt2", max_history: int = 4):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model)
        self.model = GPT2LMHeadModel.from_pretrained(model)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.eval()
        self.history: List[Tuple[str, str]] = []
        self.max_history = max_history

    def build_prompt(self, user_message: str) -> str:
        """Construct the text prompt sent to the language model.

        The prompt contains an initial instruction followed by the
        preserved conversation history (if any) and the new user
        message. The assistant response position is left open so the
        model can complete it.
        """

        prompt = (
            "The following is a conversation with an intelligent AI assistant. "
            "The assistant is helpful, clear, and educational.\n\n"
        )

        for user, agent in self.history:
            prompt += f"User: {user}\n"
            prompt += f"Assistant: {agent}\n"

        prompt += f"User: {user_message}\nAssistant:"
        return prompt

    def answer(self, user_message: str) -> str:
        """Generate an assistant response for `user_message`.

        This method builds the prompt, tokenizes it, runs the model
        generation (sampling with temperature/top-k/top-p), decodes
        the generated tokens and extracts the assistant's reply from
        the completed text. The user/assistant pair is appended to
        the internal history and trimmed to `max_history`.
        """

        prompt = self.build_prompt(user_message)

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=80,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                repetition_penalty=1.2,
                pad_token_id=self.tokenizer.eos_token_id
            )

        generated_text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        # Extract the assistant reply from the generated completion.
        answers = generated_text.split("Assistant:")[-1].strip()

        # Stop at next user turn if the model started a new "User:" block.
        if "User:" in answers:
            answers = answers.split("User:")[0].strip()

        self.history.append((user_message, answers))

        if len(self.history) > self.max_history:
            self.history.pop(0)

        return answers