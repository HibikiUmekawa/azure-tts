# Azure Speech 音声生成サンプル（Python 版 / SSML 入力）

このプロジェクトは **Azure Cognitive Services Speech SDK** を使って、
SSML（.xml）から日本語音声を生成するサンプルです。
実行時に `draft/` 配下の XML ファイル名を入力し、音声ファイル（.wav）を `output/` に保存します。

---

## 🎯 機能概要

- **Azure Speech Service（Text-to-Speech）** を使用
- **日本語話者**（Nanami, Mayu, Keiko, Aoi, Naoki, Keita）に対応
- **入力**: `draft/` 配下の SSML（.xml）を実行時に指定
- **出力**: `output/<xmlファイル名>.wav`（ディレクトリは自動作成）
- `.env` に API キーを保存（安全管理）

---

## 📦 セットアップ手順

### 1️⃣ プロジェクトのクローン

```bash
git clone <YOUR_REPOSITORY_URL>
cd azure_tts_sample
```

---

### 2️⃣ 仮想環境（venv）の作成と有効化

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows（PowerShell）

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

### 3️⃣ 依存パッケージのインストール

以下のいずれかでインストールしてください。

```bash
pip install azure-cognitiveservices-speech python-dotenv
# もしくは requirements.txt がある場合
pip install -r requirements.txt
```

---

### 4️⃣ `.env` の作成

Azure ポータルで「Speech」リソースを作成し、
キーとリージョンを取得して `.env` ファイルを作成します。

```bash
AZURE_SPEECH_KEY=あなたのキー
AZURE_SPEECH_REGION=japaneast
```

---

### 5️⃣ SSML（XML）ファイルを `draft/` に用意

`draft/` フォルダに SSML ファイル（例: `text1-1.xml`）を配置します。
ファイルは `<speak>...</speak>` を含む SSML 形式を想定しています。

簡単な例:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="ja-JP">
  こんにちは。Azure の音声合成です。
  <break time="300ms"/>
  本日は SSML から音声を生成します。
</speak>
```

---

### 6️⃣ 実行

```bash
python main.py
```

実行するとファイル名の入力を求められます。`draft/` 配下の XML 名を拡張子付きで入力してください。

例:

```
🎯 読み込む XML ファイル名を入力してください（例: text5-2.xml）: text1-1.xml
```

生成された音声は `output/text1-1.wav` に保存されます。

---

## 🎙️ 音声の選択について

現在の実装ではデフォルトで **Nanami**（`ja-JP-NanamiNeural`）を使用します（`main.py` の `idx = 0`）。
他の話者に変更したい場合は、`main.py` の `idx` を変更してください。

利用可能な日本語音声（一部）:

- [0] `ja-JP-NanamiNeural` - 明るく元気な女性
- [1] `ja-JP-MayuNeural` - 幼めで柔らかい声（ずんだもん風）
- [2] `ja-JP-KeikoNeural` - 穏やかで優しい女性
- [3] `ja-JP-AoiNeural` - 落ち着いた女性（ニュース向け）
- [4] `ja-JP-NaokiNeural` - 自然で聞き取りやすい男性
- [5] `ja-JP-KeitaNeural` - 若めで明るい男性

---

## 🎵 出力結果

- 出力ファイル名: `output/<xml名>.wav`
- 出力場所: `output/` ディレクトリ（自動作成）
- ファイル形式: WAV（SDK のデフォルト設定）

---

## 📚 依存パッケージ

```txt
azure-cognitiveservices-speech
python-dotenv
```

---

## 💡 注意事項

- `.env` ファイルは **絶対に Git にコミットしない** でください。
- Azure Speech Service の利用には課金が発生します。
- 音声・言語の一覧は [Microsoft 公式ドキュメント](https://learn.microsoft.com/azure/cognitive-services/speech-service/language-support?tabs=tts) を参照してください。

---

## 🧩 プロジェクト構成

```
azure_tts_sample/
├── main.py
├── draft/              # 入力用 SSML（.xml）を置く
├── output/             # 生成される .wav の出力先
├── .env                # 自分で作成（キーとリージョン）
└── README.md
```

---

## 🧠 作者メモ

- Python: 3.9〜3.13 推奨
- Azure Speech SDK version: 最新
- 動作確認環境: macOS / Windows

---

## 🔗 参考

- [Azure Speech SDK for Python](https://learn.microsoft.com/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python)
- [Microsoft Neural Voice List](https://learn.microsoft.com/azure/cognitive-services/speech-service/language-support#text-to-speech)

---
