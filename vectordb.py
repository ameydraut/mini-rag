import random
import math
def chunking(text , chunk_size, overlap):
    chunks=[]
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = start+ (chunk_size-overlap)
    return chunks

def fakeEmbeddings(text,size=10):
    embeddings=[]
    for i in range(size):
        embeddings.append(random.uniform(-1,1))
    return embeddings

def cosineSimilarity(vec1,vec2):
    if len(vec1) != len(vec2):
        return 0
    
    dot = 0
    lenght1 = 0
    lenght2 = 0
    
    for i in range(len(vec1)):
        dot += vec1[i] * vec2[i]
        lenght1 += vec1[i]**2
        lenght2 += vec2[i]**2

    if lenght1 == 0 or lenght2 == 0:
        return 0
    
    return dot / (math.sqrt(lenght1) * math.sqrt(lenght2))

def vector_DB(db,chunk,embedding):
    entry = {
        "id" : len(db),
        "chunk" : chunk,
        "embedding" : embedding
    }
    db.append(entry)

def searchDB(query,db,topK):
    scoreStore = []
    query_embedding = fakeEmbeddings(query)
    for entry in db:
        similarity = cosineSimilarity(query_embedding , entry["embedding"] )
        s = {
            "score" : similarity,
            "chunk_text" : entry["chunk"]
        }
        scoreStore.append(s)
    scoreStore.sort(key=lambda x: x["score"],reverse=True)
    
    return scoreStore[:topK]

def generateAnswer(query,db):
    data=(searchDB(query,db,2))
    summary = data[0]["chunk_text"]
    answer = f"Summary based on the querry : {summary}"
    return answer 

vecDB = []
vector_DB(vecDB, "Hello world", fakeEmbeddings("Hello world"))
vector_DB(vecDB, "I like momos", fakeEmbeddings("momos"))
vector_DB(vecDB, "Python is fun", fakeEmbeddings("Python"))
print(searchDB("food", vecDB,3))
output = generateAnswer("Hello world",vecDB)
print(output)