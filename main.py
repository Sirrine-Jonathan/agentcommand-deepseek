from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from auto_gptq import AutoGPTQForCausalLM
import torch

app = FastAPI()

MODEL_DIR = "/models/deepseek-coder-33B-instruct-GPTQ"

# Load tokenizer + quantized model
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, trust_remote_code=True)
model = AutoGPTQForCausalLM.from_quantized(
    MODEL_DIR,
    trust_remote_code=True,
    device="cuda:0",
    use_safetensors=True,
    torch_dtype=torch.float16
)
model.eval()

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 512

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt").to("cuda")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=request.max_tokens)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}