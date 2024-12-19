from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from typing import List, Dict
import torch


class Chat:
    def __init__(self, model_name: str):
        """
        Initializes the Chat class with the specified model.
        :param model_name: Name of the model to load.
        """
        self.conversation_history: List[Dict[str, str]] = []
        self.model_name = model_name

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map="cpu"
            )
            self.generator = pipeline(
                "text-generation",
                model=self.model,
                tokenizer=self.tokenizer,
                max_new_tokens=512
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load model or tokenizer: {e}")

    def add_message(self, role: str, content: str) -> None:
        """
        Adds a message to the conversation history.
        :param role: Role of the message sender ('user' or 'assistant').
        :param content: The content of the message.
        """
        if role not in ['user', 'assistant']:
            raise ValueError("Role must be either 'user' or 'assistant'.")
        message = {'role': role, 'content': content}
        self.conversation_history.append(message)

    def generate_response(self) -> str:
        """
        Generates a response from the model based on the conversation history.
        :return: The generated response.
        """
        if not self.conversation_history:
            raise ValueError(
                "Conversation history is empty. Add a message first.")

        # Format the conversation for the model input
        formatted_input = self._format_conversation_history()

        try:
            outputs = self.generator(
                formatted_input,
                pad_token_id=self.tokenizer.eos_token_id
            )
            response = outputs[0]['generated_text']
            # Add response to the conversation history
            self.add_message('assistant', response)
            return response
        except Exception as e:
            raise RuntimeError(f"Failed to generate response: {e}")

    def _format_conversation_history(self) -> str:
        """
        Formats the conversation history into a single string for the model.
        :return: Formatted conversation history.
        """
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history])

    def reset_conversation(self) -> None:
        """
        Clears the conversation history.
        """
        self.conversation_history = []


new_chat = Chat("meta-llama/Llama-3.2-1B")

new_chat.add_message("user", "What is your name?")

response = new_chat.generate_response()

print(response)  # Output: "assistant: My name is Llama, the pirate chatbot!"
