import pandas as pd
import os

all_answers = []
all_scores = []
file_names = []
# with open('all','rb')as file_answers:
#     for ans in file_answers.read().splitlines():
#         all_answers.append(ans)

root_dir = 'D:\GP\match_answers\data\scores'

for subdir, dirs, files in os.walk(root_dir):
    f = []
    for file in files:
        if os.path.join(subdir, file).endswith('ave'):
            with open(os.path.join(subdir, file), 'r') as file_scores:
                for s in file_scores.read().splitlines():
                    f.append(s)
    all_scores.append(f)
all_scores.remove([])

root_dir = 'D:\GP\match_answers\data\student_answers'

for file in os.listdir(root_dir):
    file_names.append(file)
    f = []
    with open(os.path.join(root_dir, file), 'rb') as file_scores:
        for s in file_scores.read().splitlines():
            f.append(s)
    all_answers.append(f)

# clean
a = []
cleaned_answers = []
for i in all_answers:
    a = []
    for j in i:
        x = str(j)
        answ = x.replace(x.split(' ')[0], '').replace(x[-1], '').replace('<br>','')
        a.append(answ)
    cleaned_answers.append(a)

# create files

for index, i in enumerate(cleaned_answers):
    # print(i)
    # print(len(all_scores[index]))
    data = pd.DataFrame(columns=['answers', 'score'])
    data['score'] = all_scores[index]
    data['answers'] = i
    data.to_csv('grading_answers/'+file_names[index]+'.csv',index=False)


