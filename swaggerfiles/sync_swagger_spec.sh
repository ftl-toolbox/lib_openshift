#!/bin/bash

DEFAULT_ENDPOINT='https://localhost:8443/swaggerapi'
SWAGGER_ENDPOINT=${1-$DEFAULT_ENDPOINT}

curl -o swagger.json ${SWAGGER_ENDPOINT}/ -k

sed -i -e 's/"path": "\/\(.*\)",/"path": "\1\/swagger.json",/' swagger.json

for api in /apis /version /api/v1 /api /apis/extensions/v1beta1 /apis/extensions /apis/autoscaling/v1 /apis/autoscaling /apis/batch/v1 /apis/batch /oapi/v1 /osapi /oapi /controllers /healthz /healthz/ready; do
  curl -o .${api}/swagger.json ${SWAGGER_ENDPOINT}${api} -k;
done

for file in `find . -name swagger.json`; do
  sed -i -e 's/"type": "any"/"type": "object"/g' $file
  sed -i -e "s#${SWAGGER_ENDPOINT%/*}#https://localhost:8443#" $file
done
