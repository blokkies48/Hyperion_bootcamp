
import spacy
# Code extract 1
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Code extract 2
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Code extract 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", similarity)

# Cat - monkey: 0.5929930210113525
# cat - banana: 0.2235882580280304
# monkey - banana: 0.4041501581668854

# chimpanzee - monkey: 0.8372925519943237
# banana - chimpanzee: 0.3217780888080597

# My example
tokens = nlp('chimpanzee apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# As stated in the notes cat and monkey have a higher score due to them being 
# both animals, but still different types of animals so the score isn't 
# that high. In my own example I replaced the word cat with chimpanzee.
# I noticed that chimpanzee and monkey have higher scores due to them being 
# both of in the same animal family (don't quote me on that). What I also found 
# interesting is that banana and chimpanzee have lower scores. Could be that 
# spacy realizes monkeys tent to the banana fiends and chimps prefer different foods.
# (don't quote me on that). 

# Noticed with the simpler language model. gives a lower overall score. I believe that
# it is due to error received stating no word vectors loaded so the results will be 
# based on other factors giving a less accurate score.