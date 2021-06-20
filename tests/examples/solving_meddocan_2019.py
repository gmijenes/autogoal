# # Solving the MEDDOCAN challenge

# This script runs an instance of [`AutoML`](/api/autogoal.ml#automl)
# in the [MEDDOCAN 2019 challenge](https://github.com/PlanTL-SANIDAD/SPACCC_MEDDOCAN).
# The full source code can be found [here](https://github.com/autogoal/autogoal/blob/main/docs/examples/solving_meddocan_2019.py).

# | Dataset | URL |
# |--|--|
# | MEDDOCAN 2019 | <https://github.com/PlanTL-SANIDAD/SPACCC_MEDDOCAN> |

# ## Experimentation parameters
#
# This experiment was run with the following parameters:
#
# | Parameter | Value |
# |--|--|
# | Total epochs         | 1      |
# | Maximum iterations   | 10000  |
# | Timeout per pipeline | 30 min |
# | Global timeout       | -      |
# | Max RAM per pipeline | 20 GB  |
# | Population size      | 50     |
# | Selection (k-best)   | 10     |
# | Early stop           |-       |

# The experiments were run in the following hardware configurations
# (allocated indistinctively according to available resources):

# | Config | CPU | Cache | Memory | HDD |
# |--|--|--|--|--|
# | **A** | 12 core Intel Xeon Gold 6126 | 19712 KB |  191927.2MB | 999.7GB  |
# | **B** | 6 core Intel Xeon E5-1650 v3 | 15360 KB |  32045.5MB  | 2500.5GB |
# | **C** | Quad core Intel Core i7-2600 |  8192 KB |  15917.1MB  | 1480.3GB |

# !!! note
#     The hardware configuration details were extracted with `inxi -CmD` and summarized.

# ## Relevant imports

# Most of this example follows the same logic as the [UCI example](/examples/solving_uci_datasets).
# First the necessary imports

from autogoal.ml import AutoML
from autogoal.datasets import meddocan
from autogoal.search import (
    RichLogger,
    PESearch,
)
from autogoal.kb import *

# ## Parsing arguments

# Next, we parse the command line arguments to configure the experiment.

# The default values are the ones used for the experimentation reported in the paper.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--iterations", type=int, default=10000)
parser.add_argument("--timeout", type=int, default=1800)
parser.add_argument("--memory", type=int, default=20)
parser.add_argument("--popsize", type=int, default=50)
parser.add_argument("--selection", type=int, default=10)
parser.add_argument("--global-timeout", type=int, default=None)
parser.add_argument("--examples", type=int, default=None)
parser.add_argument("--token", default=None)
parser.add_argument("--channel", default=None)

args = parser.parse_args()

print(args)

# ## Experimentation

# Instantiate the classifier.
# Note that the input and output types here are defined to match the problem statement,
# i.e., entity recognition.

from autogoal.contrib import find_classes

classifier = AutoML(
    search_algorithm=PESearch,
    input=(Seq[Seq[Word]], Supervised[Seq[Seq[Label]]]),
    output=Seq[Seq[Label]],
    registry=find_classes(exclude="Keras|Bert"),
    search_iterations=args.iterations,
    score_metric=meddocan.F1_beta,
    cross_validation_steps=1,
    pop_size=args.popsize,
    search_timeout=args.global_timeout,
    evaluation_timeout=args.timeout,
    memory_limit=args.memory * 1024 ** 3,
)

# Basic logging configuration.

loggers = [RichLogger()]

if args.token:
    from autogoal.contrib.telegram import TelegramLogger

    telegram = TelegramLogger(token=args.token, name=f"MEDDOCAN", channel=args.channel,)
    loggers.append(telegram)

# Finally, loading the MEDDOCAN dataset, running the `AutoML` instance,
# and printing the results.

X_train, y_train, X_test, y_test = meddocan.load(max_examples=args.examples)

classifier.fit(X_train, y_train, logger=loggers)
score = classifier.score(X_test, y_test)

print(score)
