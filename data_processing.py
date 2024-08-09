from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, BertTokenizer, BertForTokenClassification, AutoModelForSequenceClassification, AutoTokenizer
import re

class DataProcessing:
    def __init__(self):
        self.ner_pipeline = self.load_ner_model()
        self.sentiment_pipeline = self.load_sentiment_model()

    def load_ner_model(self):
        model_name = 'akdeniz27/bert-base-turkish-cased-ner'
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model = BertForTokenClassification.from_pretrained(model_name)
        return pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy='simple')

    def load_sentiment_model(self):
        model_name = 'gurkan08/turkish-product-comment-sentiment-classification'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        return pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    def clean_text(self, text):
        """Clean the input text by removing URLs, trimming whitespace, and normalizing spaces."""
        text = re.sub(r'http\S+', '', text)  # Remove URLs
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        return text.strip()  # Trim leading and trailing whitespace

    def smart_extract_entities(self, text):
        """Extract entities from text based on capitalization or special symbols (e.g., '@')."""
        ner_results = self.ner_pipeline(text)
        entities = []

        current_entity = []
        for word in text.split():
            if word[0].isupper() or word.startswith("@"):
                current_entity.append(word)
            else:
                if current_entity:
                    entities.append(' '.join(current_entity))
                    current_entity = []
        if current_entity:
            entities.append(' '.join(current_entity))
        return entities

    def extract_sentiment(self, text):
        """Analyze sentiment of the text and return it in Turkish."""
        sentiment_result = self.sentiment_pipeline(text)[0]
        sentiment_label = sentiment_result['label'].lower()

        # Translate sentiment labels to Turkish
        sentiment_mapping = {
            'positive': 'olumlu',
            'negative': 'olumsuz',
            'neutral': 'nötr'
        }
        return sentiment_mapping.get(sentiment_label, 'bilinmiyor')  # 'bilinmiyor' for unknown labels

    def process_text(self, text):
        """Process the input text to extract cleaned text, entities, and their sentiment."""
        cleaned_text = self.clean_text(text)
        entities = self.smart_extract_entities(cleaned_text)
        sentiment = self.extract_sentiment(cleaned_text)

        results = [{"entity": entity, "sentiment": sentiment} for entity in entities]

        return {

            "entity_list": entities,
            "results": results
        }