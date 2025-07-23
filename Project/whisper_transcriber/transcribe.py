import whisper
import argparse
import os

def transcribe(audio_path, model_size="small"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"File not found: {audio_path}")

    print(f" Loading model '{model_size}'...")
    model = whisper.load_model(model_size)

    print("️ Converting audio to text...")
    result = model.transcribe(audio_path, language="fa")

    print("\nRecognized text:")
    print(result["text"])

    output_path = os.path.splitext(audio_path)[0] + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"\nText saved to file.: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Persian medical audio to text")
    parser.add_argument("--input_audio", type=str, help="Audio file path (wav, mp3, m4a...)")
    parser.add_argument("--model_size", type=str, default="small", help="اندازه مدل Whisper (tiny, base, small, medium, large)")
    args = parser.parse_args()


    audio_file = args.input_audio if args.input_audio else "audios/sample 2.wav"
    transcribe(audio_file, args.model_size)
