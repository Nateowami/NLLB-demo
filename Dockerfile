FROM python:3.9

# Install steps mostly taken from https://medium.com/mlearning-ai/text-translation-using-nllb-and-huggingface-tutorial-7e789e0f7816

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install -U pip transformers
RUN pip install sentencepiece
RUN pip install fasttext

COPY import_modal.py .

RUN python import_modal.py

COPY nllb.py .

CMD ["python", "nllb.py"]
