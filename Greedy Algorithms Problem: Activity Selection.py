def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])

    return selected_activities

activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
print("Selected activities:", activity_selection(activities))
