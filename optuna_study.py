import optuna
import json 
from tunables import get_all_tunables 
import random

f = open('./search_space.json')
search_space = json.load(f)
f.close()

total_trials = search_space["total_trials"]
objective_function = search_space["objective_function"]
direction = search_space["direction"]
tunables = search_space["tunables"]
print(total_trials)

def objective(trial):
    experiment_tunables = []
    for tunable in tunables:
                if tunable["value_type"].lower() == "double":
                    tunable_value = trial.suggest_discrete_uniform(
                        tunable["name"], tunable["lower_bound"], tunable["upper_bound"], tunable["step"]
                    )
                elif tunable["value_type"].lower() == "integer":
                    tunable_value = trial.suggest_int(
                        tunable["name"], tunable["lower_bound"], tunable["upper_bound"], tunable["step"]
                    )
                elif tunable["value_type"].lower() == "categorical":
                    tunable_value = trial.suggest_categorical(tunable["name"], tunable["choices"])

                experiment_tunables.append({"tunable_name": tunable["name"], "tunable_value": tunable_value})
    
    print(experiment_tunables)  
    score =experiment_tunables[0]["tunable_value"] ** 2 + experiment_tunables[1]["tunable_value"]
    return score

sampler = optuna.samplers.TPESampler(seed=10)
study = optuna.create_study(direction=direction, sampler=sampler)
study.optimize(objective, n_trials=total_trials)
