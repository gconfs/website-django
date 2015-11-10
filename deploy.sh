#!/usr/bin/zsh

cd $( dirname $0 )

[ $# -lt 2 ] && echo "Give me a db and a user" &&  exit 1

db=$1
user=$2


sed -i "s/DB/$db/" psql_dump.sh
sed -i "s/USER/$user/" psql_dump.sh
