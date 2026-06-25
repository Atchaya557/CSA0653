#Atchaya Vharsne S (192524185)

jobs = [
    {"name": "J1", "duration": 2, "deadline": 3},
    {"name": "J2", "duration": 1, "deadline": 2},
    {"name": "J3", "duration": 2, "deadline": 4}
]

employees = ["E1", "E2"]

# Store assigned jobs for each employee
schedule = {emp: [] for emp in employees}

# Check whether a job can be assigned safely
def is_safe(emp, job):
    current_time = sum(j["duration"] for j in schedule[emp])

    # Check deadline constraint
    if current_time + job["duration"] > job["deadline"]:
        return False

    return True

# Backtracking function
def job_scheduling(job_index):
    if job_index == len(jobs):
        return True

    job = jobs[job_index]

    for emp in employees:
        if is_safe(emp, job):

            # Assign job
            schedule[emp].append(job)

            # Recur for next job
            if job_scheduling(job_index + 1):
                return True

            # Backtrack
            schedule[emp].pop()

    return False

# Main
if job_scheduling(0):
    print("Feasible Schedule Found:\n")

    for emp in employees:
        print(emp, "->", end=" ")
        for job in schedule[emp]:
            print(job["name"], end=" ")
        print()
else:
    print("No feasible schedule exists")
