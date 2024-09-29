from chunky import __version__, App
import customtkinter as ctk


class GuiApp(ctk.CTk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.geometry("600x400")
		self.title("Chunky")

		self.heading = ctk.CTkLabel(self, text="Chunky Task Helper", font=ctk.CTkFont("Roboto", 30, 'bold'))
		self.heading.pack(fill='both')

		self.task_input = ctk.CTkEntry(self, placeholder_text="Enter your task here:")
		self.task_input.pack(fill='both')

		self.task_input_button = ctk.CTkButton(self, text="Generate Steps", command=self.submit)
		self.task_input_button.pack(fill='both')

		self.content_frame = ctk.CTkTextbox(self)
		self.content_frame.pack(fill='both')

		self.app = App(input("Please enter your token: "))

	def submit(self):
		output = self.app.run(self.task_input.get())
		self.content_frame.delete("1.0", ctk.END)
		self.content_frame.insert("1.0", "\n".join(output))


if __name__ == "__main__":
	print(f"Chunky v{__version__}")
	ctk.set_default_color_theme("green")
	app = GuiApp()
	app.mainloop()
