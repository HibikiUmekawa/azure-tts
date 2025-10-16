import os
from pathlib import Path
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
# 📖 XML の内容を読み込む関数
# ===================================================
def read_text_file(file_path: Path) -> str:
    if not file_path.exists():
        print(f"❌ 指定されたファイルが見つかりません: {file_path}")
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

# ===================================================
# 🔧 音声合成関数
# ===================================================
def synthesize_speech(text: str, voice_index: int, output_file: Path):
    if not text:
        print(f"⚠️ 読み上げるテキストが空です: {output_file.stem}")
        return

    voice_info = JAPANESE_VOICES[voice_index]
    voice_name = voice_info["name"]

    print(f"\n🎤 [{voice_index}] {voice_name} - {voice_info['desc']}")
    print(f"🔊 {output_file.stem}.xml の内容を音声に変換中...")

    # Azure Speech 設定
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = voice_name
    audio_config = speechsdk.audio.AudioOutputConfig(filename=str(output_file))

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_ssml_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"✅ 出力完了: {output_file.name}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print(f"❌ エラー: {cancellation.reason}")
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print(f"詳細: {cancellation.error_details}")

# ===================================================
# 🧠 実行部
# ===================================================
if __name__ == "__main__":
    draft_dir = Path(__file__).parent / "draft"
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    # 音声選択（Nanami固定なら idx=0）
    idx = 0

    # -------------------------------
    # 🔹 ユーザーがXMLファイル名を指定
    # -------------------------------
    filename = input("🎯 読み込む XML ファイル名を入力してください（例: text5-2.xml）: ").strip()
    xml_path = draft_dir / filename

    if not xml_path.exists():
        print(f"❌ ファイルが見つかりません: {xml_path}")
    else:
        ssml_text = read_text_file(xml_path)
        output_file = output_dir / (xml_path.stem + ".wav")
        synthesize_speech(ssml_text, voice_index=idx, output_file=output_file)
        print("\n🎉 音声ファイルの生成が完了しました！")
