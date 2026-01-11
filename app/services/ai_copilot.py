from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class AICopilotService:
    @staticmethod
    def ask(question: str, context: str = "") -> dict:
        """
        Sends question + context to OpenAI API and returns:
        - text answer
        - visual form for guidance
        """
        prompt = f"{context}\n\nUser Question: {question}\nAnswer with instructions and visual guidance."

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful Ventyy assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        answer = response.choices[0].message.content
        # Example visual form (dummy)
        return {
            "text": answer,
            "visual_form": {"type": "dummy_form", "fields": ["example_field1", "example_field2"]}
        }
