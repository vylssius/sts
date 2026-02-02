from elevenlabs import ElevenLabs, save


class ElevenLabsTTS:
    def __init__(self, api_key, voice_id):
        self.client = ElevenLabs(api_key=api_key)
        self.voice_id = voice_id

    def generate(self, text, file_path="voice.wav"):
        print("🔊 Generating voice...")

        audio = self.client.text_to_speech.convert(
            voice_id=self.voice_id,
            model_id="eleven_monolingual_v1",
            text=text,
            output_format="wav_16000",  # ✅ FIXED HERE
        )

        save(audio, file_path)
        return file_path
