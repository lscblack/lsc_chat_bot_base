# LSC Chatbot Base

Build a local, private chatbot trained on your own documents using [Ollama](https://ollama.com), [nomic-embed-text](https://ollama.com/library/nomic-embed-text) for embeddings, and local LLMs like [Qwen3](https://huggingface.co/qwen), [Nous Hermes 2 Yi](https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B), or [LLaMA 3](https://ollama.com/library/llama3) for chat responses.

---

## 🚀 Features
- ✅ Train on your own `.txt` files
- 🔍 Search using vector embeddings (`nomic-embed-text`)
- 💬 Chat with context using local models like `qwen3`, `qwen3`, `llama3`, `mistral`, `phi`, or `gemma`
- ⚡ Fast local inference via Ollama (for supported models)
- 🔁 Dynamically switch models in real-time (`/switch mistral`)
- 🖥️ CLI and FastAPI interface

---

## 📁 Project Structure
```

lsc\_chat\_bot\_base/
├── data\_loader.py       # loads .txt files from /data
├── embeddings.py        # uses nomic-embed-text to embed documents
├── vector\_db.py         # stores/query embeddings with ChromaDB
├── bot.py               # CLI chatbot interface
├── api\_server.py        # REST API using FastAPI
├── environment.yml      # required packages
├── .env                 # environment variables
├── data/                # your local document directory
└── README.md            # you're here

````

---

## ⚙️ Setup Instructions

### 1. Install Ollama
Download from: [https://ollama.com](https://ollama.com)  
Then start it:
```bash
ollama serve
````

### 2. Pull Required Models

Supported by Ollama:

```bash
ollama pull nomic-embed-text
ollama pull llama3         # or mistral, phi, gemma, nous-hermes2-yi
```

> ⚠️ **Qwen3 is currently NOT available via `ollama pull`.**
> To use Qwen3, run it locally via Hugging Face weights and an inference server like [text-generation-webui](https://github.com/oobabooga/text-generation-webui) or [vLLM](https://github.com/vllm-project/vllm).

---

### 3. Clone the Repo

```bash
git clone https://github.com/lscblack/lsc_chat_bot_base.git
cd lsc_chat_bot_base
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add Your Data

Put `.txt` files into the `data/` directory. Example:

```
data/
├── example1.txt
└── notes.txt
```

### 6. Run the CLI Chatbot

```bash
python bot.py
```

You'll see:

```
[Default model: nous-hermes2-yi]
You: 
```

💡 To switch models in chat:

```
/switch mistral
```

---

## 🌐 Run the FastAPI Server

```bash
uvicorn api_server:app --reload
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

### Sample Request:

```
POST /ask
{
  "question": "What is this bot about?"
}
```

---

## 🔄 Available Commands (CLI)

| Command           | Description               |
| ----------------- | ------------------------- |
| `/switch <model>` | Switch to a different LLM |
| `exit` or `quit`  | End the session           |

---

## 🤖 Models You Can Use

| Model           | Quality         | Speed       | Use For                                |
| --------------- | --------------- | ----------- | -------------------------------------- |
| nous-hermes2-yi | 🧠 Multilingual | Medium      | Deep knowledge, many languages         |
| qwen3 (local)   | 🧠 Multilingual | Medium-Fast | Strong multilingual, coding, reasoning |
| llama3          | 🧠 Best Q\&A    | Medium      | Deep reasoning                         |
| mistral         | ⚡ Fast          | Fast        | Chatbots, productivity, devs           |
| phi             | 🪶 Light        | Very Fast   | Basic replies, small resource use      |
| gemma           | 🌍 Balanced     | Fast        | Academic/general answers               |

To see what models you've pulled via Ollama:

```bash
ollama list
```

---

## 🧪 Example Flow

```
You: How do I train this bot?
Bot: Just add your text files into /data and run bot.py. The system embeds them with nomic-embed-text, stores them in a vector DB, and uses Nous Hermes 2 Yi to generate answers based on the most relevant chunks.

You: /switch mistral
Bot: [Switched to model: mistral]
```

---

## 📦 Deployment Suggestions

* Deploy the FastAPI app behind Nginx or serve via `gunicorn`
* Use systemd to keep `ollama` and `uvicorn` running
* Optionally expose a web UI (React/Flutter)

---

## 👨‍💻 Author

**Loue Sauveur Christian (lscblack)**
Software Engineer | AI Explorer | Entrepreneur

GitHub: [@lscblack](https://github.com/lscblack)

---

## 📜 License

MIT License — free to use, modify, share.

