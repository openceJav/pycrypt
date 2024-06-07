# https://learning.oreilly.com/videos/pytorch-ultimate-2024/9781801070089/9781801070089-video1_1/

import sys
import os
import re
import json
import requests as req
import datetime as dt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# Rich Lib
from rich import print, box
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

# Inquirer Lib
from inquirer import prompt, List, Checkbox, Text, Confirm

# PyTorch Lib
import torch
import torch.nn as nn
import torch.optim as optim

# Flask Lib
from flask import Flask, jsonify, make_response, send_from_directory, render_template, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app=app)

@app.route("/")
def hello_world():
    return render_template("index.html")


# TODO: Configure Flask Routes
# TODO: Complete PyTorch Model
# TODO: Complete PyTorch Training
# TODO: Complete PyTorch Testing
# TODO: Complete PyTorch Prediction