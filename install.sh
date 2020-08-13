#!/usr/bin/env bash

if [[ $(uname -s) != "Darwin" ]]; then
  echo "Install commands only setup for Darwin"
  exit 1
fi

if ! command -v python3; then
  brew install python3
fi

python3 -m pip install -r requirements.txt
