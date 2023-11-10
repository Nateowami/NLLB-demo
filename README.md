# A Dockerfile for running Meta's NLLB

https://ai.meta.com/research/no-language-left-behind/

## Usage

``` bash
git clone git@github.com:Nateowami/NLLB-demo.git
cd NLLB-demo
docker build -t nllb .
docker run -p 8000:8000 nllb
```

Then navigate to localhost:8000
