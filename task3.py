with open('input_data.txt') as f:
    lines = f.readlines()
n = lines[0]
player_list = []

for i in range(1, len(lines)):
    player_list.append(lines[i].strip('\n').split(" "))

total_points = []
for j in range(len(player_list)):
    points_of_freethrows = int(player_list[j][-1])
    points_of_threepoints = int(player_list[j][-2]) * 3
    points_of_twopoints = int(player_list[j][-3]) * 2
    total = points_of_freethrows + points_of_twopoints + points_of_threepoints
    total_points.append(total)

max_points = max(total_points)
max_total_points_by_player = total_points.index(max_points)
max_point_player = total_points.count(max_points)

if max_point_player >= 1:
    player_list_with_same_number_of_points = [index for index, element in enumerate(total_points) if element == max_points]
    player_with_most_points_and_lowest_number_is = player_list[min(player_list_with_same_number_of_points)][0]

get_player_minutes = []
get_player_seconds = []

for k in range(len(player_list)):
    get_player_minutes.append(int(player_list[k][1]))
    get_player_seconds.append(int(player_list[k][2]))

minutes_to_seconds = [element * 60 for element in get_player_minutes]

total_seconds = []
for x in range(0, len(get_player_seconds)):
    total_seconds.append(get_player_seconds[x] + minutes_to_seconds[x])

players_with_least_time_played = total_seconds.count(min(total_seconds))

if players_with_least_time_played >= 1:
    player_list_with_least_time_played = [index for index, element in enumerate(total_seconds) if element == min(total_seconds)]
    player_least_amount_played_ant_lowest_number = player_list[min(player_list_with_least_time_played)][0]

list_of_three_point_made = []
for i in range(len(player_list)):
    list_of_three_point_made.append(player_list[i][-2])
players_count_with_most_three_points_made = list_of_three_point_made.count(max(list_of_three_point_made))

if players_count_with_most_three_points_made >= 1:
    player_index_with_most_three_points = [index for index, element in enumerate(list_of_three_point_made) if element == max(list_of_three_point_made)]
player_with_the_most_three_points_and_lowest_number = player_list[min(player_index_with_most_three_points)][0]

list_of_two_points = []
list_of_free_throws = []
list_of_three_points = []

for i in range(len(player_list)):
    list_of_two_points.append(int(player_list[i][-3]))
    list_of_free_throws.append(int(player_list[i][-1]))
    list_of_three_points.append(int(player_list[i][-2]))
points_scored_with_two_points = sum(list_of_two_points) * 2
points_scored_with_free_throws = sum(list_of_free_throws)
points_scored_with_three_points = sum(list_of_three_points) * 3
total_points_in_game = points_scored_with_two_points + points_scored_with_free_throws + points_scored_with_three_points


with open('output_data.txt', 'w') as f:
    f.write(f"Player who scored the most points is {player_with_most_points_and_lowest_number_is} \n")
    f.write(f"Player who played least amount of time is {player_least_amount_played_ant_lowest_number} \n")
    f.write(f"Player with the most three points made is {players_count_with_most_three_points_made} \n")
    f.write(f"There was {points_scored_with_two_points} points scored by two-points \n")
    f.write(f"There was {points_scored_with_free_throws} points scored by free throws \n")
    f.write(f"Total points scored in game is {total_points_in_game} \n")
