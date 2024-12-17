from transformers import AutoTokenizer, AutoModelForCausalLM

# Lade Tokenizer und Modell
model_name = "mistralai/Mistral-7B-v0.1"  # Offizieller Modellname auf Hugging Face

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Eingabeaufforderung (Prompt)
prompt = "Erkläre mir bitte die Hauptideen der Quantenmechanik."

# Tokenisierung der Eingabe
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generiere Text mit dem Modell
output = model.generate(
    inputs["input_ids"],
    max_length=200,  # Maximale Länge des generierten Textes
    num_return_sequences=1,  # Anzahl der Sequenzen
    temperature=0.7,  # Steuerung der Kreativität
    top_p=0.9,  # Top-p-Sampling
    do_sample=True  # Zufällige Auswahl aktivieren
)

# Dekodiere und drucke das Ergebnis
result = tokenizer.decode(output[0], skip_special_tokens=True)
print(result)
