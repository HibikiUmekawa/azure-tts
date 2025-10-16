import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

speech_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SPEECH_REGION")

# ===================================================
# 🎙️ 日本語音声一覧（定数配列）
# ===================================================
JAPANESE_VOICES = [
    {"name": "ja-JP-NanamiNeural", "desc": "明るく元気な女性"},
    {"name": "ja-JP-MayuNeural", "desc": "幼めで柔らかい声（ずんだもん風）"},
    {"name": "ja-JP-KeikoNeural", "desc": "穏やかで優しい女性"},
    {"name": "ja-JP-AoiNeural", "desc": "落ち着いた女性（ニュース向け）"},
    {"name": "ja-JP-NaokiNeural", "desc": "自然で聞き取りやすい男性"},
    {"name": "ja-JP-KeitaNeural", "desc": "若めで明るい男性"},
]

# ===================================================
# 📖 text.xml の内容を読み込む関数
# ===================================================
def read_text_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        print(f"❌ 指定されたファイルが見つかりません: {file_path}")
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

# ===================================================
# 🔧 音声合成関数
# ===================================================
def synthesize_speech(text: str, voice_index: int = 1, output_file: str = "output.wav"):
    if not text:
        print("⚠️ 読み上げるテキストが空です。text.xml の中身を確認してください。")
        return

    if voice_index < 0 or voice_index >= len(JAPANESE_VOICES):
        print(f"❌ 無効な音声番号です。0〜{len(JAPANESE_VOICES)-1} の範囲で指定してください。")
        return

    voice_info = JAPANESE_VOICES[voice_index]
    voice_name = voice_info["name"]

    print(f"🎤 選択中の音声: [{voice_index}] {voice_name} ({voice_info['desc']})")

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = voice_name

    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    print(f"🔊 text.xml の内容を音声に変換中...")
    result = synthesizer.speak_ssml_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"✅ 音声ファイルを生成しました: {output_file}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print(f"❌ 音声合成に失敗しました: {cancellation.reason}")
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print(f"エラー詳細: {cancellation.error_details}")

# ===================================================
# 🧠 実行部
# ===================================================
if __name__ == "__main__":
    print("🎙️ 利用可能な日本語音声:")
    for i, v in enumerate(JAPANESE_VOICES):
        print(f"  [{i}] {v['name']} - {v['desc']}")

    # idx = int(input("番号を入力してください: "))
    idx = 0

    # text.xml の内容を読み込む
    draft_text = read_text_file("text.xml")

    synthesize_speech(draft_text, voice_index=idx)
