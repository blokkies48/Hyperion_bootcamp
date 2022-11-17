import spacy

nlp = spacy.load('en_core_web_sm')

# Got from https://www.apartmenttherapy.com/garden-sentences-262915
g_path_sentence_1 = "The horse Jonathan, raced past the barn fell."
g_path_sentence_2 = "The old man the boat."
g_path_sentence_3 = "The florist sent the flowers was pleased."
g_path_sentence_4 = "The cotton clothing is made of grows in Mississippi."
g_path_sentence_5 = "The sour drink from the ocean."

garden_path_sentences = [
    g_path_sentence_1,
    g_path_sentence_2,
    g_path_sentence_3,
    g_path_sentence_4,
    g_path_sentence_5,
    ]

for value in garden_path_sentences:
    doc = nlp(value)
    print("-----\n**Tokenise:**")
    print(doc.text.split()) # Tokenise
    print("\n**Entity recognition:**")
    print([(i, i.label_) for i in doc.ents]) # Entity recognition

# Well with my chosen sentences there is only two "Entity recognition" 
# that is given the category of Geopolitical entity (GPE) and PERSON.
# The first one was expected because it is a place defined by
# politically established borders, but the second one should be 
# a NAME or ANIMAL because it is referring to the horse.
# What I didn't expect is that there will only be two entity recognition.

