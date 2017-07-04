#!/bin/sh
find $(dirname $0) -name '*.py' -print -exec chmod +x {} \; -exec {} \;
