import re
from transformers import pipeline, BertTokenizer, BertForTokenClassification, AutoModelForSequenceClassification, AutoTokenizer

class DataProcessing:
    def __init__(self):
        self.ner_pipeline = self.load_ner_model()
        self.sentiment_pipeline = self.load_sentiment_model()

    def load_ner_model(self):
        model_name = 'akdeniz27/bert-base-turkish-cased-ner'
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model = BertForTokenClassification.from_pretrained(model_name)
        ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy='simple')
        return ner_pipeline

    def load_sentiment_model(self):
        model_name = 'gurkan08/turkish-product-comment-sentiment-classification'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
        return sentiment_pipeline

    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)  # Birden fazla boşluğu tek boşluğa indirgeme
        text = re.sub(r'http\S+', '', text)  # URL'leri kaldırma
        text = text.strip()  # Baş ve sondaki boşlukları kaldırma
        return text

    def smart_extract_entities(self, text):
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
        sentiment_results = self.sentiment_pipeline(text)
        sentiment = sentiment_results[0]['label']
        # İngilizce etiketleri Türkçe karşılıklarına çevirme
        if sentiment == 'positive':
            sentiment = 'olumlu'
        elif sentiment == 'negative':
            sentiment = 'olumsuz'
        elif sentiment == 'neutral':
            sentiment = 'nötr'
        return sentiment

    def process_text(self, text):
        cleaned_text = self.clean_text(text)
        entities = self.smart_extract_entities(cleaned_text)

        sentiment = self.extract_sentiment(cleaned_text)

        results = []
        for entity in entities:
            results.append({"entity": entity, "sentiment": sentiment})

        return {
            "cleaned_text": cleaned_text,
            "entity_list": entities,
            "results": results
        }
