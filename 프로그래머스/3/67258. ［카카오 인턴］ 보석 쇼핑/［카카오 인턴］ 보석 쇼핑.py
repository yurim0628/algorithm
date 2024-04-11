from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    num_unique_gems = len(set(gems))

    if num_unique_gems == 1:
        return [1, 1]

    gem_indices = defaultdict(list)
    start_idx, end_idx = 0, 0
    gem_count = 0

    while end_idx < len(gems):
        current_gem = gems[end_idx]
        if not gem_indices[current_gem]:
            gem_count += 1
        gem_indices[current_gem].append(end_idx)

        while gem_count == num_unique_gems:
            if end_idx - start_idx < answer[1] - answer[0]:
                answer = [start_idx, end_idx]

            start_gem = gems[start_idx]
            gem_indices[start_gem].pop(0)
            if not gem_indices[start_gem]:
                gem_count -= 1
            start_idx += 1

        end_idx += 1

    return [answer[0] + 1, answer[1] + 1]
