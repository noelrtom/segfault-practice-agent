from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
r = client.models.generate_content(model="gemini-2.5-flash", contents="Say hello in 5 words")
print(r.text)