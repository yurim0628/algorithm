N, K = map(int, input().split())
aquarium = list(map(int, input().split()))

def add_fish(aquarium):
  min_value = min(aquarium)
  
  for i in range(len(aquarium)):
    if aquarium[i] == min_value:
      aquarium[i] += 1
      
  return aquarium

def simulate(aquarium):
  row_len = len(aquarium)

  diff = [[0] * len(aquarium[row_index]) for row_index in range(row_len)]
  visited = [[0] * len(aquarium[row_index]) for row_index in range(row_len)]
    
  for cx in range(row_len):
    for cy in range(len(aquarium[cx])):
      for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
          nx, ny = cx + dx, cy + dy
          if 0<=nx<row_len and 0<=ny<len(aquarium[nx]):
            if visited[nx][ny] == 0:
              d = abs(aquarium[cx][cy] - aquarium[nx][ny]) // 5
              if d > 0:
                if aquarium[cx][cy] > aquarium[nx][ny]:
                  diff[cx][cy] -= d
                  diff[nx][ny] += d
                else:
                  diff[cx][cy] += d
                  diff[nx][ny] -= d
            visited[cx][cy] = 1

  for x in range(row_len):
    for y in range(len(aquarium[x])):
      aquarium[x][y] += diff[x][y]
      
  return aquarium

def linearize(aquarium):
  max_index = len(aquarium[-1])  
  
  linear_aquarium = []
  for col_index in range(max_index):
    for row in reversed(aquarium):
      if col_index < len(row):
        linear_aquarium.append(row[col_index])
        
  return linear_aquarium

def rotate_90_clockwise(aquarium):
  while True:
    extra_row = aquarium[-1][len(aquarium[0]):]
    
    rotated_aquarium = []
    for col_index in range(len(aquarium[0])):
        rotated_col = []
        for row in reversed(aquarium):
          rotated_col.append(row[col_index])
        rotated_aquarium.append(rotated_col)
      
    aquarium = rotated_aquarium + [extra_row]
    if len(aquarium[-1]) - len(aquarium[-2]) < len(aquarium):
        break

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
  aquarium = simulate(aquarium)
  aquarium = linearize(aquarium)
  
  aquarium = rotate_180_clockwise(aquarium)
  aquarium = simulate(aquarium)
  aquarium = linearize(aquarium)

  count += 1
  
  result = max(aquarium) - min(aquarium)
  if result <= K:
    break

print(count)