__version__ = "1.0.0"
from chunky.process import Processor
from chunky.entry import EntryHandler

SYSTEM_PROMPT = "Break down complex tasks into small, manageable steps."


class App:
	def __init__(self, token: str) -> None:
		self.token = token

	def run(self, task) -> None:
		entry_handler = EntryHandler(SYSTEM_PROMPT)
		processor = Processor(token=self.token)

		payload = entry_handler.handle_entry(task)
		return processor.query(payload)


if __name__ == "__main__":
	app = App(input("Please enter your token: "))
	task = input("What is your task? ")
	app.run(task)
