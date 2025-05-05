from flask import Flask, send_file, request, jsonify
from transformers.models.nllb.tokenization_nllb import FAIRSEQ_LANGUAGE_CODES

app = Flask(__name__)

checkpoint = 'facebook/nllb-200-distilled-600M'
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

@app.route('/')
def send_report():
    return send_file('index.html')

@app.route('/api/v1/translate/languages/', methods=['GET'])
def translate_languages():
    return list(FAIRSEQ_LANGUAGE_CODES)

@app.route('/api/v1/translate/', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        source_language = data['sourceLanguage']
        target_language = data['targetLanguage']
        text_to_translate = data['text']

        translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_language, tgt_lang=target_language, max_length=400)

        translated_text = translator(text_to_translate)[0]['translation_text']

        response = {
            'originalText': text_to_translate,
            'translatedText': translated_text
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
