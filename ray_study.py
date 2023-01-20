from ray import tune
import random
import json
from ray.air import session
from ray.tune.search.optuna import OptunaSearch


# 1. Define an objective function.
def objective(config):    
    score = config["memoryRequest"] ** 2 + config["cpuRequest"]
    return {"score": score}

# 2. Define a search space.
search_space = {
    "memoryRequest": tune.uniform(270, 4096),
    "cpuRequest": tune.quniform(1.0, 4.0, 0.1)
}

optuna_search = OptunaSearch(
    metric="score",
    mode="min",
    seed=10)

# 3. Start a Tune run and print the best result.
tuner = tune.Tuner(objective, 
                    param_space=search_space, 
                    tune_config=tune.TuneConfig(search_alg=optuna_search,
                                            num_samples=10))
results = tuner.fit()
print("Best Trial")
print(results.get_best_result( metric="score", mode="min").config)