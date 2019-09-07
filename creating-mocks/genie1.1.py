#!/usr/bin/env python3


"""
This script prepares files to create mock devices. Once these are created, user needs to create a
testbed.yaml file. See src directory for examples.
"""

from collections import defaultdict

# BEGINNING OF USER UPDATE SECTION
# Update this list for your topology
device_list = ['rtr1', 'sw1', 'sw2']

# Update this list; add/delete etc.. to create
rev_list = ['normal', 'break1', 'brk2']

# Update to point to your base testbed
testbed = 'cp-testbeds/default_testbed.yaml'

# Update these directories to suit your needs.
output_location = 'cp-snapshot'
record_location = 'cp-record-dir'
mock_location = 'cp-mock'
recordings = "outputs/recordings.txt"
# END OF USER UPDATE SECTION

dyn_lists = defaultdict(list)

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


# Use this function to test output to your screen
# Be careful this doesn't actually run the commands (if that isn't the intent)
def display(res1, res2):
    count = 0
    for r in res1:
        print(r)
        count += 1
        if count == len(res1):
            print()

    for k, v in res2.items():
        for x in range(len(v)):
            print(v[x])
    return


def make_recordings(res1, res2):
    count = 0
    for r1 in res1:
        with open(recordings, 'a') as rec:
            rec.write(r1 + '\n')
            count += 1
            if count == len(res1):
                rec.write('\n')

    for k, v in res2.items():
        for x in range(len(v)):
            with open(recordings, 'a') as rec:
                rec.write(v[x] + '\n')
    return


if __name__ == '__main__':
    result1, result2 = create_learnt()
    #display(result1, result2)
    make_recordings(result1, result2)
