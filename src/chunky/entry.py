class EntryHandler:
	def __init__(self, system_prompt):
		self.system_prompt = system_prompt

	def create_payload(self, query: str) -> dict:
		# 	return {
		# 		"inputs": f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
		# {self.system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
		# {query}<|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
		return {
			"inputs": query,
			"parameters": {
				"stream": True
			}
		}

	def handle_entry(self, task):
		# lengthquery = int(input("How many steps do you want to break it into? "))
		entry = f"Break the following task into 10steps, without describing each task, as a list that includes all of the generated, broken-down instructions in a concise manner. The task is: \"{task}\"\n\n\n"
		return self.create_payload(entry)
