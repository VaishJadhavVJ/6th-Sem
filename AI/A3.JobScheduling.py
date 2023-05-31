def schedule_jobs(jobs):
    # Sort the jobs based on their finish time in ascending order
    jobs.sort(key=lambda x: x[1])

    # Initialize the result list to store the scheduled jobs
    result = []

    # Initialize the set to track the busy time slots
    busy_slots = set()

    for job in jobs:
        start_time, finish_time = job

        # Check if the current time slot is busy
        if start_time not in busy_slots:
            # Add the job to the result list
            result.append(job)

            # Mark the time slots as busy
            for slot in range(start_time, finish_time):
                busy_slots.add(slot)

    return result


# Driver code
if __name__ == "__main__":
    # Example jobs: (start_time, finish_time)
    jobs = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 10)]

    # Schedule the jobs using the Greedy algorithm
    scheduled_jobs = schedule_jobs(jobs)

    # Print the scheduled jobs
    print("Scheduled Jobs:")
    for job in scheduled_jobs:
        print(f"Start Time: {job[0]}, Finish Time: {job[1]}")
