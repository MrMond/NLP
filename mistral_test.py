from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Dein Hugging Face Auth-Token
HF_AUTH_TOKEN = "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"

# Modellname von Hugging Face
model_name = "mistralai/Mistral-7B-v0.1"

# Tokenizer laden (mit Auth-Token)
print("Lade Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_AUTH_TOKEN)

# Modell laden (auf CPU beschränkt, mit Auth-Token)
print("Lade Modell (das kann auf der CPU etwas dauern)...")
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map="auto", 
    token=HF_AUTH_TOKEN,
    torch_dtype=torch.float16
)

# Eingabetext
input_text = "Was weißt du über Basketball"

# Eingabe tokenisieren
inputs = tokenizer(input_text, return_tensors="pt")

# Modell generieren lassen
print("Generiere Text...")
outputs = model.generate(**inputs, max_new_tokens=50, do_sample=True)

# Ausgabe dekodieren
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generierter Text:")
print(result)
