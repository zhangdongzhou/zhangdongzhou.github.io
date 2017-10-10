#!/bin/bash

git init

python ./python_ref_update/reference_list.py

git add --all
git commit -m "Publication Update"
git push -u origin master