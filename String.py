sentence = "Learning Python is fun and rewarding."

substring = sentence[-28:-14]  
print("Extracted substring:", substring)

modified_sentence = sentence.replace("rewarding", "exciting")
print("Modified sentence:", modified_sentence)
insert_position = modified_sentence.index("exciting") + len("exciting")
final_sentence = modified_sentence[:insert_position] + " Keep practicing!" + modified_sentence[insert_position:]
print("Sentence after insertion:", final_sentence)

final_output = final_sentence.title()  
print("Final output:", final_output)
