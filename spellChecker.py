# Spelling check

from textblob import TextBlob
txt = "Python programing is fun."
print("Original text:", txt)
st = TextBlob(txt)
print("Corrected text:", st.correct())