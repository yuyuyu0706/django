#!/bin/bash

DIR=`dirname ${0}`
cd $DIR

git add ./autocommit.sh
git add .
git status
git commit -m 'auto commit'
git push django master

exit 0
