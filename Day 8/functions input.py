scores = [20,30,40,50,60, 80, 100]

def analyze_scores(scores):
    highest = scores[0]
    lowest = scores[0]
    total = [0]
    passed_count = [0]

    for score in scores:
        if score > highest:
            highest = scores
        if score < lowest:
           lowest = scores
        total += score
        if score > 50:
            passed_count+= 1


    average = round(total/7)

    print("highest:", highest)
    print("lowest:", lowest)
    print("average:", average)
    print("Number of students passed:", passed_count)


analyze_scores(scores)




