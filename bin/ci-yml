#!/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import yaml
import sys


def run_subtree(arr_elems, ignore_errors=False):
    for elem in arr_elems:
        print " * " + elem # print back command...
        try:
            subprocess.check_call(elem, shell=True)
        except subprocess.CalledProcessError as e:
            if ignore_errors:
                pass
            else:
                raise e


# TODO add a lot of error checks

if __name__ == "__main__":
    stream = open(".ci.yml", "r")
    ops = yaml.load(stream)

    #print ops

    if ops.has_key('prepare'):
        run_subtree(ops['prepare'], ignore_errors=True)

    if ops.has_key('test'):
        for arg in sys.argv[1:]:
            if arg in ops['test']:
                run_subtree(ops['test'][arg])

    if ops.has_key('deploy') and 'deploy' in sys.argv[1:]:
        run_subtree(ops['deploy'])
