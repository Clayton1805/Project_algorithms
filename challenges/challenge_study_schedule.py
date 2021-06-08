def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    count = 0
    for index, start in enumerate(start_time):
        if start <= target_time <= end_time[index]:
            count += 1
    return count
# start_time = [2, 1, 2, 1, 4, 4]
# end_time   = [2, 2, 3, 5, 5, 5]
# print(study_schedule(start_time, end_time, 3))
