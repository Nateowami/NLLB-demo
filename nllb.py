# See list of locale codes at https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200
source_lang = "eng_Latn" # input("Source language (e.g. arb_Arab): ")
target_lang = "hin_Deva" # input("Target language (e.g. eng_Latn): ")
text = input("Text to translate: ")

print("Loading model...")

checkpoint = 'facebook/nllb-200-distilled-600M'
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang, tgt_lang=target_lang, max_length=400)
# reverse_translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=target_lang, tgt_lang=source_lang, max_length=400)
# Available languages can be found with tokenizer.lang_code_to_id

print("Translating " + source_lang + " to " + target_lang)

while True:
  output = translator(text)
  translated_text = output[0]['translation_text']
  print(translated_text)

  # reversed = reverse_translator(translated_text)
  # print("Reverse translated: " + reversed[0]["translation_text"])

  print()
  text = input("Text to translate: ")
