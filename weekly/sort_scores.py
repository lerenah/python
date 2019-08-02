def sort_scores(unsorted_scores, highest_possible_score):
    scores = [0] * highest_possible_score
    output = []

    for score in unsorted_scores:
        scores[score] += 1

    for score in range(highest_possible_score - 1, -1, -1):
        count = scores[score]

        for num in range(count):
            output.append(score)

    return output
