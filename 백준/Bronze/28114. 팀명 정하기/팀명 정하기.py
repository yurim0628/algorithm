score_dict = {}
years = []

for _ in range(3):
    score, year, last_name = input().split()
    score_dict[last_name] = int(score)
    years.append(year[2:])  

years.sort()
print(''.join(year for year in years))

sorted_scores = sorted(score_dict.items(), key=lambda item: item[1], reverse=True)
print(''.join(name[0] for name, score in sorted_scores))