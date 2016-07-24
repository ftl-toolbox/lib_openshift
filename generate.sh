#!/bin/bash

set -eu

BASE_PACKAGE=lib_openshift
PACKAGE_VERSION="0.0.1"

echo "{ \"packageName\": \"lib_openshift\", \"packageVersion\": \"${PACKAGE_VERSION}\" }" > swagger_codegen_config.json
java -DdebugOperations=true -DdebugModels=true -jar ~/bin/swagger-codegen-cli.jar generate -i swaggerfiles/swagger.json -l python -c swagger_codegen_config.json -t codegen_templates  --git-repo-id lib_openshift --git-user-id ftl-toolbox

sed -i -e 's/self.verify_ssl = True/self.verify_ssl = False/' lib_openshift/configuration.py
