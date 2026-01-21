from transformers import pipeline
from transformers import TextClassificationPipeline

def classify(text:str,
        classifier: TextClassificationPipeline = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
):
    return classifier(text)