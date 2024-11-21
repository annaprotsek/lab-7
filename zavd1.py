def process_sentence():
    sentence = input("Введіть рядок: ")
    words = sentence.split()  
    word_count = len(words)  
    longest_word = max(words, key=len) if words else ""  

    print(f"Кількість слів: {word_count}")
    print(f"Найдовше слово: {longest_word}")

process_sentence()
