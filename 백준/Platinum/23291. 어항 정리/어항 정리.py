N, K = map(int, input().split())
aquarium = list(map(int, input().split()))

def add_fish(aquarium):
  min_value = min(aquarium)

  for i in range(len(aquarium)):
    if aquarium[i] == min_value:
      aquarium[i] += 1

  return aquarium

def adjust(aquarium):
  high = len(aquarium)

  adjust_list = []
  for cx in range(high):
      for cy in range(len(aquarium[cx])):
          for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
              nx, ny = cx + dx, cy + dy
              if 0 <= nx < high and 0 <= ny < len(aquarium[nx]):
                  d = (aquarium[cx][cy] - aquarium[nx][ny]) // 5
                  if d > 0:
                      adjust_list.append((cx, cy, nx, ny, d))

  for cx, cy, nx, ny, d in adjust_list:
      aquarium[cx][cy] -= d
      aquarium[nx][ny] += d

  return aquarium

def linearize(aquarium):
  width = len(aquarium[0])
  
  linear_aquarium = []
  for col_index in range(len(aquarium[0])):
    for row in reversed(aquarium):
        linear_aquarium.append(row[col_index])
  linear_aquarium = linear_aquarium + aquarium[-1][width:]

  return linear_aquarium

def rotate_90_clockwise(aquarium):
  while True:
    width = len(aquarium[-2])

    if len(aquarium[-1]) - width < len(aquarium): 
      break
    
    extra_aquarium = [row[:width] for row in aquarium]
    rotated_aquarium = list(map(list, zip(*extra_aquarium[::-1])))
    aquarium = rotated_aquarium + [aquarium[-1][width:]]

  return aquarium

def rotate_180_clockwise(aquarium):
  # N/2 
  middle_index = len(aquarium) // 2

  aquarium_left = aquarium[:middle_index][::-1]
  aquarium_right = aquarium[middle_index:]

  rotated_aquarium = [aquarium_left, aquarium_right]

  # N/4
  middle_index = len(rotated_aquarium[0]) // 2

  aquarium_left_bottom = rotated_aquarium[0][:middle_index][::-1]
  aquarium_left_top = rotated_aquarium[1][:middle_index][::-1]

  aquarium_right_top = rotated_aquarium[0][middle_index:]
  aquarium_right_bottom = rotated_aquarium[1][middle_index:]

  rotated_aquarium = [aquarium_left_top, aquarium_left_bottom, aquarium_right_top, aquarium_right_bottom]

  return rotated_aquarium

count = 0

while True:
  aquarium = add_fish(aquarium)
  aquarium = [[aquarium[0]], aquarium[1:]]

  aquarium = rotate_90_clockwise(aquarium)
  aquarium = adjust(aquarium)
  aquarium = linearize(aquarium)

  aquarium = rotate_180_clockwise(aquarium)
  aquarium = adjust(aquarium)
  aquarium = linearize(aquarium)

  count += 1

  result = max(aquarium) - min(aquarium)
  if result <= K:
    break

print(count)