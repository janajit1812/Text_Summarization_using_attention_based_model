import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)
punctuation = punctuation + '\n'

nlp = spacy.load("en_core_web_sm")

main_text="""There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[3] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured."""

doc = nlp(main_text)

word_dict={}

for word in doc:
	word=word.text.lower()
	if word not in stopwords:
		if word not in punctuation:

			if word in word_dict:
				word_dict[word]+=1

			else:
				word_dict[word]=1

#print(word_dict)
#print(max(word_dict,key=word_dict.get))
max_freq=max(word_dict.values())
#print(max_freq)

for word in word_dict.keys():
    word_dict[word] = word_dict[word]/max_freq
#print(word_dict)

sentences=[]
sentence_score=0

#sentence_tokens = [sent for sent in doc.sents]


for i,sentence in enumerate(doc.sents):
	sentence_score=0
	for word in sentence:
		if word.text.lower() in word_dict.keys():
			# if sentence not in sentence_scores.keys():
			word=word.text.lower()
			sentence_score+=word_dict[word]
		
	sentences.append((i, sentence.text.replace("\n"," "), (sentence_score)))

#print(sentences)

sorted_sentence=sorted(sentences,key=lambda x: -x[2])
top_three=sorted(sorted_sentence[:4],key=lambda x: x[0])

#print(top_three)

summary_text=""

for sentence in top_three:
	summary_text +=sentence[1]+" "

print(summary_text,"\n")
sumt=len(summary_text)
mait=len(main_text)
per=(sumt/mait)*100
print("summary length :",len(summary_text),"\n")

print("main text length :",len(main_text),"\n")

print("reduction  percentage:",100-per,"% \n")


