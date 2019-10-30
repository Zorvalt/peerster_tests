#!/usr/bin/env bash

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

print_usage() {
  echo "Usage:"
  echo -e "\t$0 name"
  echo -e "\tWhere 'name' is a capital letter"
  exit 1
}

if (( $# != 1 )); then
  print_usage
fi

nameVal=$(ord "$1")
if (( nameVal < $(ord A) || nameVal > $(ord Z) )); then
  print_usage
fi

name=$1
offset=$(( nameVal - $(ord A)))
gossipPort=$(( 5000 + offset ))
uiPort=$(( 8080 + offset ))
peerPort=$(( gossipPort + 1))

go run main.go -vv -name "$name" -gossipAddr=127.0.0.1:$gossipPort -UIPort=$uiPort -GUIPort=$uiPort -peers=127.0.0.1:$peerPort -rtimer 10
