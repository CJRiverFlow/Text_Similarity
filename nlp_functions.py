from text_sim import String2Vector

def calculate_similarity(sentence1,sentence2):
    """
    Calculus of text similarity

    input = 2 string 
    output =  cosine similary in range 0-1
    """
    error = None
    sen1_vec = String2Vector(sentence1) 
    sen2_vec = String2Vector(sentence2)

    doc1 = sen1_vec.process_sentence()
    doc2 = sen2_vec.process_sentence()

    if (len(doc1)!=0) and (len(doc2)!=0):
        result = doc1.similarity(doc2)
    else:
        result = None
        error = "One or both vectors become empty after tokenization"
    
    return result, error