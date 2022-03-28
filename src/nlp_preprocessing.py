import nltk
import string
import re
import unicodedata


def clean_text(text: str) -> str:
    """Realiza a limpeza do texto passando para o formato minúsculo e removendo
    caracteres indesejados.

    Args:
        text (str): texto a ser limpo

    Returns:
        str: texto limpo
    """    
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('\w*\d\w*', ' ', text)

    return text

def remove_accents(text: str) -> str:
    """Remoção de ascentos e caracteres especiais

    Args:
        text (str): texto a ser processado

    Returns:
        str: texto sem ascento
    """    
    nfkd_form = unicodedata.normalize("NFKD", text)
    ascii_form = nfkd_form.encode("ASCII", "ignore").decode()
    return ascii_form


# instanciando a lista de stopwords
stopwords = nltk.corpus.stopwords.words("portuguese")
stopwords = [remove_accents(word) for word in stopwords]

# instanciando o stemmer do nltk para a língua portuguesa
stemmer = nltk.stem.RSLPStemmer()

def custom_tokenizer(text: str) -> list[str]:
    """Realiza a tokenizaçao customizada, composta por eliminação de stopwords
    e tokens curtos, stemming e remoção de ascentos.

    Args:
        text (str): texto a ser tokenizado

    Returns:
        list[str]: lista de tokens
    """    
    token_list = nltk.tokenize.word_tokenize(text=text, language="portuguese")
    stem_list = [stemmer.stem(token)
                 for token in token_list
                 if token not in stopwords and len(token) > 2]
    
    return [remove_accents(stem) for stem in stem_list]

def preprocess_txt(txt: str) -> str:
    """Executa o pre-processamento textual padrão

    Args:
        txt (str): texto a ser preproessado

    Returns:
        str: texto padronizado
    """
    cleaned_txt = clean_text(txt)
    token_txt = custom_tokenizer(cleaned_txt)
    return " ".join(token_txt)