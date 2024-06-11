from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class BARTParaphraser:
    def __init__(self):
        self.model_name = "eugenesiow/bart-paraphrase"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def paraphrase(self, text):
        inputs = self.tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=1024,
            num_beams=5,
            num_return_sequences=1,
            early_stopping=True
        )
        paraphrased_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return paraphrased_text
