import os
import re

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

model_type = "sentiment_analysis"

reviews_train = []
for line in open('../movie_data/full_train.txt', 'r', encoding="utf8"):
    reviews_train.append(line.strip())

reviews_test = []
for line in open('../movie_data/full_test.txt', 'r', encoding="utf8"):
    reviews_test.append(line.strip())

target = [1 if i < 12500 else 0 for i in range(25000)]

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
NO_SPACE = ""
SPACE = " "

def preprocess_reviews(reviews):

    reviews = [REPLACE_NO_SPACE.sub(NO_SPACE, line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(SPACE, line) for line in reviews]

    return reviews

def infer_model(model_type, text):
    stop_words = ['in', 'of', 'at', 'a', 'the']
    dataset = "../models/" + model_type + ".sav"
    vectorizer = CountVectorizer(binary=True, ngram_range=(1, 3), stop_words = stop_words)
    loaded_model = joblib.load(dataset)
    result = loaded_model.predict(vectorizer.transform([text]))
    
    return result



dataset = "../models/" + model_type + ".sav"
loaded_model = joblib.load(dataset)
print(loaded_model.predict(["I went and saw this movie last night after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge."])[0])
print(loaded_model.predict(["My boyfriend and I went to watch The Guardian.At first I didn't want to watch it, but I loved the movie- It was definitely the best movie I have seen in sometime.They portrayed the USCG very well, it really showed me what they do and I think they should really be appreciated more.Not only did it teach but it was a really good movie. The movie shows what the really do and how hard the job is.I think being a USCG would be challenging and very scary. It was a great movie all around. I would suggest this movie for anyone to see.The ending broke my heart but I know why he did it. The storyline was great I give it 2 thumbs up. I cried it was very emotional, I would give it a 20 if I could!"])[0])
print(loaded_model.predict(["If you had asked me how the movie was throughout the film, I would have told you it was great! However, I left the theatre feeling unsatisfied. After thinking a little about it, I believe the problem was the pace of the ending. I feel that the majority of the movie moved kind of slow, and then the ending developed very fast. So, I would say the ending left me disappointed.<br /><br />I thought that the characters were well developed. Costner and Kutcher both portrayed their roles very well. Yes! Ashton Kutcher can act! Also, the different relationships between the characters seemed very real. Furthermore,I thought that the different plot lines were well developed. Overall, it was a good movie and I would recommend seeing it.<br /><br />In conclusion: Good Characters, Great Plot, Poorly Written/Edited Ending. Still, Go See It!!!"])[0])
