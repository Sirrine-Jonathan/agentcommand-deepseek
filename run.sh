#!/bin/bash

MODEL_DIR="/models/deepseek-coder-33B-instruct-GPTQ"

if [ ! -d "$MODEL_DIR" ]; then
  echo "🔁 Downloading Deepseek-Coder 33B Instruct  (4-bit)..."
  mkdir -p $MODEL_DIR
	git lfs install
  git clone https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-GPTQ $MODEL_DIR
fi

echo "✅ Model is ready."
echo "🚀 Starting server..."
uvicorn main:app --host 0.0.0.0 --port 8000