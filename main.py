import os
from assistant import MimirAssistant

AZURE_KEY = os.getenv("AZURE_TTS_KEY")
AZURE_REGION = os.getenv("AZURE_TTS_REGION")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "7fbQ7yJuEo56rYjrYaEh"

if __name__ == "__main__":
    assistant = MimirAssistant(
        AZURE_KEY,
        AZURE_REGION,
        OPENAI_KEY,
        ELEVENLABS_KEY,
        VOICE_ID
    )

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    assistant.run()
