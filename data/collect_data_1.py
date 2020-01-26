import pandas as pd
answers = []
questions = []
with open('answers', 'r')as file_answers:
    for ans in file_answers.read().splitlines():
        answers.append(ans)


with open('questions', 'r')as file_questions:
    for q in file_questions.read().splitlines():
        questions.append(q)

print(len(answers))
print(len(questions))

# clean
cleaned_questions = []
cleaned_answers = []
for q in questions:
    x = q.replace(' <STOP>', '')
    x = x.replace(x.split(' ')[0], '')
    cleaned_questions.append(x)
for ans in answers:
    x = ans.replace(' <STOP>', '')
    x = x.replace(x.split(' ')[0], '')
    cleaned_answers.append(x)

data = pd.DataFrame(columns=['questions','answers'])
data['questions'] = cleaned_questions
data['answers'] = cleaned_answers
data.to_csv('Mohlar_Data.csv')
