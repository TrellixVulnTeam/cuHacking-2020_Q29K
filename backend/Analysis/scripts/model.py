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
        for line in reviews_train:
            print(line)

        return reviews_train, reviews_test, target

    if model_t == "technicality_analysis":
        print("technical parsing")
    if model_t == "relevancy_analysis":
        print("relevancy_analysis")

def preprocess_reviews(reviews):
    REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)")
    REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    NO_SPACE = ""
    SPACE = " "
    reviews = [REPLACE_NO_SPACE.sub(NO_SPACE, line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(SPACE, line) for line in reviews]
    
    return reviews

def train_model(model_type, reviews_train_clean, reviews_test_clean):
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
    final = LinearSVC(C=0.01)
    final.fit(X, target)
    joblib.dump(final, filename)
    print ("Final Accuracy: %s" 
        % accuracy_score(target, final.predict(X_test)))
    return final, ngram_vectorizer

def infer_model(text, model):
    result = model.predict([text])[0]
    return result

def load_model(model_type):
    dataset = "../models/" + model_type + ".sav"
    loaded_model = joblib.load(dataset)
    return loaded_model

model = load_model("sentiment_analysis")
print(infer_model("I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge.", model))
