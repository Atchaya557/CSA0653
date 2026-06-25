# Atchaya Vharsne S (192524185)

def is_safe(exam, graph, colors, slot):
    for neighbor in range(len(graph)):
        if graph[exam][neighbor] == 1 and colors[neighbor] == slot:
            return False
    return True

def graph_coloring(graph, m, colors, exam):
    if exam == len(graph):
        return True

    for slot in range(1, m + 1):
        if is_safe(exam, graph, colors, slot):

            colors[exam] = slot

            if graph_coloring(graph, m, colors, exam + 1):
                return True

            colors[exam] = 0

    return False

# Conflict Graph
graph = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

num_slots = 3
colors = [0] * len(graph)

if graph_coloring(graph, num_slots, colors, 0):
    print("Exam Schedule:")
    for i in range(len(colors)):
        print("Exam", i + 1, "-> Time Slot", colors[i])
else:
    print("No feasible schedule exists")
