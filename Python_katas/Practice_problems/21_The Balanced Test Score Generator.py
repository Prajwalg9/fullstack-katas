import random

def BalancedTestScore():
    scores=[]
    scores.append(random.randint(1,34))
    scores.append(random.randint(70,80))
    scores.append(100)
    for i in range(17):
        scores.append(random.randint(1, 100))
    random.shuffle(scores)
    return scores
print(BalancedTestScore())


