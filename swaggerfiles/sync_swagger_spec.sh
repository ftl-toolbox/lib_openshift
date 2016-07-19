#!/bin/bash

DEFAULT_ENDPOINT='https://localhost:8443/swaggerapi'
SWAGGER_ENDPOINT=${1-$DEFAULT_ENDPOINT}

curl -s -o swagger.json ${SWAGGER_ENDPOINT}/ -k

sed -i -e 's/"path": "\/\(.*\)",/"path": "\1\/swagger.json",/' swagger.json

for api in $(grep path swagger.json | cut -d '"' -f 4 | sed -e s_/swagger.json__); do
  curl -s -o ./${api}/swagger.json ${SWAGGER_ENDPOINT}/${api} -k;
done

for file in `find . -name swagger.json`; do
  sed -i -e 's/"type": "any"/"type": "object"/g' $file
  sed -i -e 's/"nickname": "connect/"nickname": "/g' $file
  sed -i -e "s#${SWAGGER_ENDPOINT%/*}#https://localhost:8443#" $file
done
