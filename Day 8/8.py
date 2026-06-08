scores =[40,50,60,70,80,90]

def analyze_scores(scores):
    highest = scores[0]
    lowest = scores[0]
    total= 0
    passed_count = 0
    for score in scores:
        if highest > score:
            highest = score
        if lowest < score:
            lowest = score
            total += score
            passed_count += 1


   average = round(total / 6)
   print("highest" score:"highest")

