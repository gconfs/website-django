#!/usr/bin/zsh

cd $( dirname $0 )
pip install -r requirements.txt

[ $# -lt 2 ] && exit 0

db=$1
user=$2


sed -i "s/DB/$db/" psql_dump.sh
sed -i "s/USER/$user/" psql_dump.sh
