quiz_scores=[99, 87, 91, 72, 77]

average1=(sum(quiz_scores)/len(quiz_scores))
print(average1)



scores1=[88, 92, 90, 75, 62]

scores2=[62, 70, 78, 99, 100]

for index in range(len(scores1)):
    print(f'{scores1[index]} times {scores2[index]} equals {scores1[index] * scores2[index]}')