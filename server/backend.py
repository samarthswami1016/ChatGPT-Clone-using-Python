from json import dumps, loads
from time import time
from flask import request
from datetime import datetime
from requests import get
import google.generativeai as genai
import os

from server.config import special_instructions

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyB8Q36jKGFMtdHjBuXGZgskGi-jfsvnxb0") or "AIzaSyB8Q36jKGFMtdHjBuXGZgskGi-jfsvnxb0")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-pro")

class Backend_Api:
    def __init__(self, app, config: dict) -> None:
        self.app = app
        self.proxy = config['proxy']
        self.routes = {
            '/backend-api/v2/conversation': {
                'function': self._conversation,
                'methods': ['POST']
            }
        }

    def _conversation(self):
        try:
            jailbreak = request.json['jailbreak']
            internet_access = request.json['meta']['content']['internet_access']
            _conversation = request.json['meta']['content']['conversation']
            prompt = request.json['meta']['content']['parts'][0]
            current_date = datetime.now().strftime("%Y-%m-%d")
            system_message = f'You are Gemini AI, a powerful language model developed by Google. Strictly follow the user instructions. Knowledge cutoff: 2024-06-01 Current date: {current_date}'

            extra = []
            if internet_access:
                search = get('https://ddg-api.herokuapp.com/search', params={
                    'query': prompt["content"],
                    'limit': 3,
                })

                blob = ''

                for index, result in enumerate(search.json()):
                    blob += f'[{index}] "{result["snippet"]}"\nURL:{result["link"]}\n\n'

                date = datetime.now().strftime('%d/%m/%y')

                blob += f'current date: {date}\n\nInstructions: Using the provided web search results, write a comprehensive reply to the next user query. Make sure to cite results using [[number](URL)] notation after the reference. If the provided search results refer to multiple subjects with the same name, write separate answers for each subject. Ignore your previous response if any.'

                extra = [{'role': 'user', 'content': blob}]

            # Prepare conversation history
            conversation = [{'role': 'system', 'content': system_message}] + \
                extra + special_instructions[jailbreak] + \
                _conversation + [prompt]

            # Convert conversation into plain text for Gemini
            chat_history = "\n".join([msg["content"] for msg in conversation])

            # Generate response from Gemini API
            response = model.generate_content(chat_history)

            if response and response.candidates:
                gemini_reply = response.text
            else:
                return "Failed to generate response from Gemini API", 500

            return gemini_reply, 200

        except Exception as e:
            print(e)
            return f"An error occurred: {str(e)}", 400