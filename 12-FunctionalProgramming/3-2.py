sentence = 'I completely agree with you'
result = list(map(lambda word: len(word), sentence.split()))

print("Text:", sentence)
print("No. of letters in words:", result)