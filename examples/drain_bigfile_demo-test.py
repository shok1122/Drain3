# SPDX-License-Identifier: MIT

import json
import logging
import os
import subprocess
import sys
import time
from os.path import dirname

from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from drain3.file_persistence import FilePersistence

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

in_log_file = "SSH-test.log"

persistence = FilePersistence("drain3_state-bigfile-train.bin")

config = TemplateMinerConfig()
config.load(dirname(__file__) + "/drain3.ini")
config.profiling_enabled = True
template_miner = TemplateMiner(persistence, config)

with open(in_log_file) as f:
    lines = f.readlines()

automaton = {}

prev_cluster_id = None
for line in lines:
    line = line.rstrip()
    line = line.partition(": ")[2]
    cluster = template_miner.match(line)
    if cluster is None:
        print(f"No match found")
    else:
        #template = cluster.get_template()
        #print(f"Matched template #{cluster.cluster_id}: {template}")
        #
        curr_cluster_id = cluster.cluster_id
        if prev_cluster_id is not None:
            if prev_cluster_id not in automaton:
                automaton[prev_cluster_id] = {}
            if curr_cluster_id not in automaton[prev_cluster_id]:
                automaton[prev_cluster_id][curr_cluster_id] = { "count": 0 }
            automaton[prev_cluster_id][curr_cluster_id]["count"] += 1
        prev_cluster_id = curr_cluster_id

print(automaton)

for k1 in automaton:
    total = sum(automaton[k1][k2]["count"] for k2 in automaton[k1])
    for k2 in automaton[k1]:
        automaton[k1][k2]["ratio"] = automaton[k1][k2]["count"] / total

print("-------")

print(automaton)
