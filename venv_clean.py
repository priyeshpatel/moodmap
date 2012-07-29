#!/bin/sh

WORKING_DIR=./
ACTIVATE_PATH=./venv/bin/activate
MY_PATH="`dirname \"$0\"`"
MY_PATH="`( cd \"$MY_PATH\" && pwd)`"

cd $MY_PATH
cd $WORKING_DIR
. $ACTIVATE_PATH
exec python clean.py
