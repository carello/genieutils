#!/usr/bin/env python3


"""
# This script prepares files for Genie. Once these are created, user needs to create a
# "cp-testbeds/mock_break(x)_testbed.yaml" file to run the demo

# Example for cp-testbeds/mock_break1_tb.yaml

testbed:
  name: cp-mock-break1

devices:

  sw2:
    alias: sw2
    os: iosxe
    type: IOSv
    connections:
      defaults:
        class: unicon.Unicon
      mock:
        command: mock_device_cli --os iosxe --mock_data_dir cp-mock/break1/sw2 --state connect
        protocol: unknown

    custom:
      abstraction:
        order: [os, type]

# Run demos per github.com/carello/netdevops_demos/genie-cli-1/
"""

from collections import defaultdict

dyn_lists = defaultdict(list)

# Update this list for your topology
device_list = ['rtr1', 'rtr2', 'sw1', 'sw2', 'sw3']

# Update this list - add/delete etc.. to create
rev_list = ['normal', 'break1']

# Update to point to your base testbed (I used VIRL to create this)
testbed = 'cp-testbeds/default_testbed.yaml'

# Update these directories to suit your needs.
output_location = 'cp-snapshot'
record_location = 'cp-record-dir'
mock_location = 'cp-mock'
recordings = "outputs/recordings.txt"


cmd0 = "genie learn all"
cmd1 = "python -m unicon.playback.mock"


def create_learnt():
    do_learn_list = list()

    for rev in rev_list:
        do_learn_list.append("{0} --testbed-file {1} --output {2}/{3} --record {3}/{4}".format(cmd0, testbed,
                                                                                               output_location, rev,
                                                                                               record_location, rev))
        for device in device_list:
            recorded_data = "{0}/{1}/{2}".format(record_location, rev, device)
            output = "{0}/{1}/{2}/{3}-{4}.yaml".format(mock_location, rev, device, device, rev)
            dyn_lists[rev].append("{0} --recorded-data {1} --output {2}".format(cmd1, recorded_data, output))
    return do_learn_list, dyn_lists


def display(res1, res2):
    # Consider writing output to a file for execution
    for r in res1:
        print(r)
    print()

    for k, v in res2.items():
        for x in range(len(v)):
            print(v[x])
    return


def make_recordings(res1, res2):
    for r1 in res1:
        with open(recordings, 'a') as rec:
            rec.write(r1 + '\n')

    with open(recordings, 'a') as rec:
        rec.write('\n')

    for k, v in res2.items():
        for x in range(len(v)):
            with open(recordings, 'a') as rec:
                rec.write(v[x] + '\n')
    return


result1, result2 = create_learnt()
#display(result1, result2)
make_recordings(result1, result2)
