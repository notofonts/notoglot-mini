#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Noto Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
Information about Unicode scripts, for the Noto project and beyond.
"""

from pathlib import Path
import json

__version__ = "0.1.0"

DATA_DIR = Path(Path(__file__).parent, "data")

def LoadScripts(base_dir=DATA_DIR):
    return json.load(open(Path(base_dir, "notoglot_scripts.json")))
