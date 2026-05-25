"""Entrypoint to start the chatbot Gradio interface.

This module provides a minimal entrypoint that imports and launches
the application defined in `view.view`. Use `python main.py` to
run the server locally.
"""

from view.view import launch


def main() -> None:
	"""Launch the Gradio chatbot application.

	Defined as a function to make it easy to import from other modules
	and to allow test harnesses to call the entrypoint without running
	the server automatically at import time.
	"""

	launch()


if __name__ == "__main__":
	main()