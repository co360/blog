#!/usr/bin/env bash
# First setup on a new computer
git submodule update --init --recursive
pip3 install -t .pip pelican
pip3 install -t .pip markdown