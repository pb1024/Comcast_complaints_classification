import nltk
from nltk.corpus import stopwords
import re

def clean_str(string):
    """
    Perform string cleaning for text data
    by removing special characters 
    and converting to lower case
    """
    string = re.sub(r"[^A-Za-z0-9()!?\'\`%$]", " ", string) # keep also %$ but removed comma
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    stiing = re.compile('<.*?>').sub('', string) #Remove HTML tags/markups
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " ( ", string)
    string = re.sub(r"\)", " ) ", string)
    string = re.sub(r"\?", " ? ", string)
    string = re.sub(r"\$", " $ ", string) #yes, isolate $
    string = re.sub(r"\%", " % ", string) #yes, isolate %
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r'\d',' ',string) #matches any digit from 0 to 100000..., \D matches non-digits
    string = re.sub(r'\s+',' ',string) #\s matches any whitespace, \s+ matches multiple whitespace, \S matches non-whitespace
    
    # removing non ascii
    string = re.sub(r'[^\x00-\x7F]+', "", string)
        
    return string.strip().lower()


def stopword(string):
    a= [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)

def text_preprocess(string):
    return stopword(clean_str(string))