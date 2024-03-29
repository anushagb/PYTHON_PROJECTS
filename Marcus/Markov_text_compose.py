
import random

def build_markov_chain(text):
    words = text.split()
    chain = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word not in chain:
            chain[current_word] = []
        
        chain[current_word].append(next_word)
    
    return chain

def generate_text(markov_chain, length=90, start_word=None):
    if start_word is None:
        start_word = random.choice(list(markov_chain.keys()))

    current_word = start_word
    generated_text = [current_word]

    for _ in range(length - 1):
        if current_word in markov_chain:
            next_word = random.choice(markov_chain[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

# Example
text_corpus = " This is a sample text for the Markov chain text composer.I am anusha from mrit student from swapnodaya trust pursiving internship in pacewisdom solutions"

markov_chain = build_markov_chain(text_corpus)
generated_text = generate_text(markov_chain, length=2000)

print(generated_text)
