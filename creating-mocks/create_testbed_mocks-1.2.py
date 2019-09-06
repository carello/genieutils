#!/usr/bin/env python3

import csv
from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

j2_env = Environment(loader=FileSystemLoader('templates'))

name = "cp-mock-normal"

# Edit this to point to your .csv file
csv_src = "data3.1.csv"

# Edit this for your needs
mock_file = "outputs/mock-break-zz.yaml"

tmpl_0 = j2_env.get_template('tmpl_0.j2')
tmpl_A = j2_env.get_template('tmpl_A.j2')

header = (tmpl_0.render(
    NAME=name
))

with open(mock_file, 'w') as fh:
    fh.write(header)

data = list()
# CSV format is MS-DOS, 
with open(csv_src, newline='') as f:
    reader = csv.DictReader(f)
    for r in reader:
        info = (r['DEVICE'], r['ALIAS'], r['OS'], r['TYPE'], r['CLASS'], r['COMMAND'], r['PROTOCOL'], r['ORDER'])
        content = (tmpl_A.render(
            DEVICE=info[0],
            ALIAS=info[1],
            OS=info[2],
            TYPE=info[3],
            CLASS=info[4],
            COMMAND=info[5],
            PROTOCOL=info[6],
            ORDER=info[7]
        ))

        with open(mock_file, 'a') as fw:
            fw.write(content)
