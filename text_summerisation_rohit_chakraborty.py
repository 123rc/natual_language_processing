import fitz
from gensim.summarization import summarize,keywords
doc = fitz.open('D:\Operations Management.pdf')
text = ""
for page in doc:
   text+=page.get_text()
#print(text)
summary = summarize(text,word_count=500)
print(summary)