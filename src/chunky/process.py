import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"


def format_output(json_output: dict) -> list:
	text = json_output[0]["generated_text"]
	_, steps = text.split("\n\n\n")
	return steps.split("\n")


class Processor:
	def __init__(self, token: str) -> None:
		self._token = token
		self.headers = {
			"Authorization": f"Bearer {self._token}",
			"Content-Type": "application/json"
		}

	def query(self, payload: dict) -> dict:
		response = requests.post(API_URL, headers=self.headers, json=payload)
		return format_output(response.json())
