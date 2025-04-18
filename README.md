# DeepSeek Coder API

This is a minimal API wrapper for the [DeepSeek Coder 33B Instruct (GPTQ)](https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-GPTQ) model using FastAPI. Built for deployment on RunPod or local environments.

---

## 🧠 Features
- Simple `/chat` endpoint for model inference
- Health check via `/health`
- Auto downloads the model if not already mounted

---

## 🚀 Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Sirrine-Jonathan/agentcommand-deepseek.git
cd agentcommand-deepseek
```

### 2. Build Docker Image
```bash
docker build -t deepseek-coder-api .
```

### 3. Run Container
```bash
docker run --gpus all -p 8000:8000 deepseek-coder-api
```

You can also map a local model directory like this:
```bash
docker run --gpus all -p 8000:8000 -v $(pwd)/models:/models deepseek-coder-api
```

---

## 🏓 Endpoints

### POST `/chat`
```json
{
  "prompt": "def fibonacci(n):",
  "max_tokens": 256
}
```

Returns:
```json
{
  "response": "def fibonacci(n):\n    if n <= 1: return n\n    return fibonacci(n-1) + fibonacci(n-2)"
}
```

### GET `/health`
Returns `{"status": "ok"}` when the server is up and model is ready.

---

## 🧊 RunPod Config
The `config.json` file is ready to go. Update the `volumeMountPath` and `MODEL_PATH` if you choose a different quantized model.

---

## 🧩 Requirements
- A GPU with at least **48GB VRAM** (e.g. A40, A100)
- CUDA 11.8 compatible runtime

---

## 🛠️ Tech Stack
- FastAPI
- Hugging Face Transformers
- torch + CUDA

---

## 📂 File Structure
```
.
├── Dockerfile
├── main.py
├── requirements.txt
├── run.sh
├── config.json
└── README.md
```

---

## 📜 License
MIT

