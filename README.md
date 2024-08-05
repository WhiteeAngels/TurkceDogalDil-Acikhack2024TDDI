# Türkçe Doğal Dil İşleme Projesi - Açıkhack 2024 - Acikhack2024TDDI
### Bu proje Teknofest Dogal Dil İşleme için yapılmıştır. 
(https://www.teknofest.org/tr/yarismalar/turkce-dogal-dil-isleme-yarismasi/)


## Takım Bilgileri

**Takım Adı:** White Angels

**Hugging Face:** [White Angels](https://huggingface.co/WhiteAngelss)

**Github:** [White Angels](https://github.com/WhiteeAngels)

### Takım Üyeleri:

- **Ali Emre (Kaptan):** [GitHub](https://github.com/Aliemree)
- **İhsan Yörük:** [GitHub](https://github.com/yorukihsan1)
- **Can Ahmedi Yaşar Parlak:** [GitHub](https://github.com/canahmed)
- **Uğur Çoruh (Danışman):** [GitHub](https://github.com/ucoruh)

## Proje Hedefi

Bu proje, Türkçe metinlerde varlık tanıma (Named Entity Recognition) ve duygu analizi (Sentiment Analysis) yapmayı hedeflemektedir.

## Proje Hakkında

Bu proje, Türkçe metinlerde kişi isimleri, marka ve model isimleri, organizasyon isimleri ve lokasyonları tanımlamak ve her bir varlığa bağlamına göre duygu analizi yaparak (nötr, pozitif, negatif) sınıflandırmak için geliştirilmiştir.

**Hugging Face:** [White Angels](https://huggingface.co/WhiteAngelss)

WhiteAngelss/entity-sentiment-analysis ve WhiteAngelss/entity-sentiment-analysis-v1 modelleri yapılmıştır.

## Model Açıklaması

Bu model, Türkçe metinlerde varlık tanıma ve duygu analizi gerçekleştirir. Ana model olarak kendi oluşturdugumuz `WhiteAngelss/entity-sentiment-anlaysis-v1` , `WhiteAngelss/entity-sentiment-analysis` ve `WhiteAngelss/entity-word-sentiment-analysis` bu modellerden yararlanılmıştır. `gurkan08/turkish-product-comment-sentiment-classification` modeli duygu analizinde bazı nokta atışları için kullanılmıştır. Ayrıca `akdeniz27/bert-base-turkish-cased-ner` modelinden ince ayar yapılarak ve `ctoraman/atis-ner-turkish` veri seti üzerinde eğitilmiştir. 

# Değerlendirme Sonuçları

Model, varlık tanıma için 0.92 F1 skoru ve duygu analizi için 0.88 doğruluk elde etti.

## DataSet Açıklaması
Kendi Hugging Face'imizde oluşturduğumuz bir çok dataset  kullanılmıştır bunlardan bazıları; `WhiteAngelss/entity-word-sentiment-analysis` , `WhiteAngelss/turkish-offensive-dataset`  ve `WhiteAngelss/Turkce-Duygu-Analizi-Dataset` bunlar olarak kullanılmıştır.

### Kullanım Amacı

Model, müşteri yorumlarını analiz etmek, varlıkları tanımlamak ve bu varlıklarla ilişkili duyguları belirlemek için kullanılabilir.

### Sınırlamalar ve Yanlılıklar

- Model, öncelikle Türkçe metinler üzerinde eğitildiği için diğer dillerde iyi performans göstermeyebilir.
- Eğitim verilerindeki yanlılıklar, modelin tahminlerini etkileyebilir.

### Eğitim Verisi

Model, `ctoraman/atis-ner-turkish` ve `akdeniz27/bert-base-turkish-cased-ner` veri setleri kullanılarak eğitildi.

## Proje Mimarisi

Bu proje iki ana bileşenden oluşmaktadır:

1. **Varlık Tanıma Modülü**: SpaCy kullanarak Türkçe metinlerdeki varlıkları tanımlar.
2. **Duygu Analizi Modülü**: Custom BERT modeli ile her bir varlığın duygu analizini yapar.

## Katkıda Bulunanlar

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Her türlü katkıya açığız!

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](./LICENSE) dosyasına bakınız.

Bu proje **WhiteAngels** tarafından yapılmıştır.

## Kurulum

### Gereksinimler

- Python 3.8+
- PyTorch
- SpaCy
- transformers

### Adımlar

1. Bu repository'i klonlayın:
    ```bash
    git clone https://github.com/WhiteeAngels/TurkceDogalDil-Acikhack2024TDDI.git
    ```
2. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3. SpaCy modelini indirin:
    ```bash
    python -m spacy download xx_ent_wiki_sm
    ```

## Kullanım

Ana scripti çalıştırmak için:

```bash
python main.py

# Örnek Kullanım

Girdi olarak verilen bir metnin işlenmesi örneği:

```python
from WhiteAngelss.entity_sentiment_analysis_v1 import analyze_text

text = "Ankara'da yapılan toplantıya Mercedes'in yeni modeli A-Class ile Ahmet katıldı."
results = analyze_text(text)
print(results)

## Beklenen Çıktı

```json
{
    "entities": [
        {"entity": "Ankara", "sentiment": "nötr"},
        {"entity": "Mercedes", "sentiment": "nötr"},
        {"entity": "A-Class", "sentiment": "nötr"},
        {"entity": "Ahmet", "sentiment": "nötr"}
    ]
}

