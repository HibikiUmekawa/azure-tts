# Azure Speech 音声生成サンプル（Python 版）

このプロジェクトは **Azure Cognitive Services Speech SDK** を使って  
テキストから日本語音声を生成するサンプルです。  
`draft.text` に入力した文章を読み上げ、音声ファイル（.wav）として保存します。

---

## 🎯 機能概要

- Azure Speech Service（Text-to-Speech）を使用
- 日本語話者（Nanami, Mayu, Keiko, Aoi, Naoki, Keita）に対応
- 読み上げるテキストは `draft.text` から自動読み込み
- `.env` に API キーを保存（安全管理）
- 依存パッケージは `requirements.txt` で管理

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

```bash
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

### 5️⃣ 読み上げテキストを用意

`draft.text` を同じフォルダに作成し、読み上げたい内容を入力します。

例：

```
こんにちは、ずんだもんなのだ！
今日はAzureで音声を作ってみたのだ。
```

---

### 6️⃣ 実行

```bash
python main.py
```

コンソール上で音声番号を選択すると、  
`output.wav` が生成されます。

例：

```
🎙️ 利用可能な日本語音声:
  [0] ja-JP-NanamiNeural - 明るく元気な女性
  [1] ja-JP-MayuNeural - 幼めで柔らかい声（ずんだもん風）
  ...
番号を入力してください: 1
```

---

## 🎵 出力結果

- 出力ファイル名: `output.wav`
- 出力場所: スクリプトと同じディレクトリ
- ファイル形式: WAV（16kHz, mono）

---

## 📚 依存パッケージ

`requirements.txt` にて管理しています。

```txt
azure-cognitiveservices-speech
python-dotenv
```

---

## 💡 注意事項

- `.env` ファイルは **絶対に Git にコミットしない** でください。
- Azure Speech Service の利用には課金が発生します。
- 日本語音声の利用可能なリストは [Microsoft 公式ドキュメント](https://learn.microsoft.com/azure/cognitive-services/speech-service/language-support?tabs=tts) を参照してください。

---

## 🧩 構成ファイル一覧

```
azure_tts_sample/
├── main.py
├── draft.text
├── requirements.txt
├── .env                # 自分で作成
└── README.md
```

---

## 🧠 作者メモ

- Python: 3.9〜3.12 推奨
- Azure Speech SDK version: 最新
- 動作確認環境: macOS / Windows

---

## 🔗 参考

- [Azure Speech SDK for Python](https://learn.microsoft.com/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python)
- [Microsoft Neural Voice List](https://learn.microsoft.com/azure/cognitive-services/speech-service/language-support#text-to-speech)

---
