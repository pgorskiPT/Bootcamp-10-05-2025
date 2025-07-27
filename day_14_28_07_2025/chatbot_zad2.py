import os
from dotenv import load_dotenv
#  git restore --staged ../.env

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

print("OPENAI_API_KEY=", api_key)
# OPENAI_API_KEY= None
