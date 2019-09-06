#!/usr/bin/env python3

import csv
from jinja2 import Template

name = "cp-mock-normal"
mock_file = "outputs/mock-break-x.yaml"

# don't change spacing or lines in the templates!!!
tmpl_0 = Template(u'''\
testbed:
  name: {{ NAME }}

devices:    


''')

tmpl_A = Template(u'''\
  {{ DEVICE }}:
    alias: {{ ALIAS }}
    os: {{ OS }}
    type: {{ TYPE }}
    connections:
      defaults:
        class: {{ CLASS }}
      mock:
        command: {{ COMMAND }}
        protocol: {{ PROTOCOL }}

    custom:
      abstraction:
        order: {{ ORDER }}


''')


header = (tmpl_0.render(
    NAME=name
))

with open(mock_file, 'w') as fh:
    fh.write(header)

data = list()
# CSV format is MS-DOS
with open("data3.1.csv", newline='') as f:
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
