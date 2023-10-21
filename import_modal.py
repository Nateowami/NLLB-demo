# This file exists because:
# 1. Documentation for using transformers often shows how to download them in Python
# 2. We want the download of the model to happen as part of the building of the image, not when it runs

checkpoint = 'facebook/nllb-200-distilled-600M'
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
