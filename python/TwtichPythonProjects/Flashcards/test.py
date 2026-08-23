

data  = [{'name': 'Math', 'questions': [{'question': 'What is 7 × 8?', 'answer': '56'}, {'question': 'What is the square root of 81?', 'answer': '9'}, {'question': 'What is 15 + 27?', 'answer': '42'}]}]

print(data[0]['questions'])

questions =  []

answers  = [] 
for  info in data[0]['questions']:
    questions.append(info['question'])
    answers.append(info['answer'])



    

    

