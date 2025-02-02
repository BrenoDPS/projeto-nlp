import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

df = pd.read_csv("../../data/processed/reclamacoes.csv")


def limpar_texto(texto):
    if not isinstance(texto, str):  # Verifica se o valor não é string
        return ""

    texto = texto.lower()
    # Remover caracteres especiais e números
    texto = re.sub(r"[^a-z\s]", "", texto)
    # Tokenização
    tokens = word_tokenize(texto)
    # Remover stopwords e aplicar lematização
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)


# Aplicar a função à coluna de texto (ajuste o nome da coluna conforme necessário)
df["texto_limpo"] = df["CDESCR"].apply(limpar_texto)

print(df["texto_limpo"].head())
