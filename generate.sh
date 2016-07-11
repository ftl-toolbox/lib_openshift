#!/bin/bash

java -jar ~/bin/swagger-codegen-cli.jar generate -i swaggerfiles/swagger.json -l python -c swagger_codegen_config.json

sed -i -e 's/self.verify_ssl = True/self.verify_ssl = False/' lib_openshift/configuration.py
