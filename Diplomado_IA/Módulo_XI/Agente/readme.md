# AGENT-GPT2

An intelligent conversational chatbot built with GPT-2, Python, HuggingFace Transformers, and Gradio.

This project was developed as part of an Artificial Intelligence diploma course to demonstrate how a language model can be used to create an intelligent conversational agent with memory and a graphical interface.

---

# Features

- Conversational AI using GPT-2
- Chatbot-style graphical interface
- Context memory for multi-turn conversations
- Built with Python and Gradio
- Educational implementation for AI and NLP learning
- Easy to extend and customize

---

# Project Structure

```bash
AGENT-GPT2/
│
├── agent/
│   ├── AgentGPT2.py
│
├── view/
│   ├── view.py
│
├── docs/
│   ├── AgentGPT2.md
│   ├── main.md
│   ├── view.md
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Technologies Used  
- Python  
- HuggingFace Transformers  
- PyTorch  
- Gradio  

---

# Installation  

Clone the repository:  

```bash
git clone https://github.com/jpachecosenard1999/Agent-GPT2
```

Enter the project folder:  

```bash
cd AGENT-GPT2
```

Install dependencies:  

```bash
pip install -r requirements.txt
```

---

# Running the Project  

Run the main file:  

```bash
python main.py
```

The chatbot interface will open in your browser.  

---

# How It Works  

The chatbot works using a GPT-2 language model.  

The agent includes:  

- Perception: receives user input  
- Memory: stores recent conversation history  
- Reasoning: generates responses using GPT-2  
- Action: returns responses to the interface  

The system builds prompts dynamically using previous conversation context.  

---

# Example  

User:  

  What is artificial intelligence?  

Agent:  

  Artificial intelligence is a field of computer science focused on creating systems capable of performing tasks that norma  

---

# Educational Purpose  

This project is intended for:  

- Artificial Intelligence courses
- NLP demonstrations
- Educational chatbot development
- Prompt engineering experiments
- GPT-based conversational systems
- Possible Improvements
- Add GPT-3 or GPT-4 API support
- Voice recognition
- Database memory
- User authentication
- Better conversation context management
- Multi-agent architecture

--- 

# License  

This project is for educational purposes.

---

# Author  

MsC. Jorge Alberto Pacheco Senard  
Centro de Investigación en Computación  
Instituto Politécnico Nacional  
jpachecos2024@cic.ipn.mx  