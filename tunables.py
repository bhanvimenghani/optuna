import json 


def get_all_tunables(search_space_json):
    f = open('search_space_json')
    search_space = json.load(f)
    f.close()


    total_trials = search_space["total_trials"]
    objective_function = search_space["objective_function"]
    direction = search_space["direction"]
    tunables = search_space["tunables"]
    print(total_trials)
    return  total_trials, direction, objective_function, tunables

