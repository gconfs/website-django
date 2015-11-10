cd $( dirname $0 )

date=$( date -I )
folder=$( echo $date | cut -d- -f 1-2 )

mkdir -p "$folder"

pg_dump -Fc -w -h localhost -d 'gconfs-website-db' -U 'corwin' -f "$folder/$date.psql"
