import os
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

model_type = "sentiment_analysis"
break_point = 12500
size_dataset = 25000

def create_dataset(model_t, break_p, size):
    if model_t == "sentiment_analysis":
        reviews_train = []
        for line in open('../movie_data/full_train.txt', 'r', encoding="utf8"):
            reviews_train.append(line.strip())
    
        reviews_test = []
        for line in open('../movie_data/full_test.txt', 'r', encoding="utf8"):
            reviews_test.append(line.strip())
        
        target = [1 if i < break_p else 0 for i in range(size)]
    if model_t == "technicality_analysis":
        print("technical parsing")
    if model_t == "relevancy_analysis":
        print("relevancy_analysis")
        
create_dataset(model_type, break_point, size_dataset)

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
NO_SPACE = ""
SPACE = " "

def preprocess_reviews(reviews):
    
    reviews = [REPLACE_NO_SPACE.sub(NO_SPACE, line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(SPACE, line) for line in reviews]
    
    return reviews

reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)

stop_words = ['in', 'of', 'at', 'a', 'the']
ngram_vectorizer = CountVectorizer(binary=True, ngram_range=(1, 3), stop_words=stop_words)
ngram_vectorizer.fit(reviews_train_clean)
X = ngram_vectorizer.transform(reviews_train_clean)
X_test = ngram_vectorizer.transform(reviews_test_clean)

X_train, X_val, y_train, y_val = train_test_split(
    X, target, train_size = 0.75
)

for c in [0.001, 0.005, 0.01, 0.05, 0.1]:
    svm = LinearSVC(C=c)
    svm.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" 
           % (c, accuracy_score(y_val, svm.predict(X_val))))



filename = "../models/" + model_type + ".sav"

joblib.dump(svm, filename)

final = LinearSVC(C=0.01)
final.fit(X, target)
print ("Final Accuracy: %s" 
       % accuracy_score(target, final.predict(X_test)))
