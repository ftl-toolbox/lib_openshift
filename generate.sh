#!/bin/bash

set -eu

BASE_PACKAGE=lib_openshift
PACKAGE_VERSION="0.0.1"

#pushd swaggerfiles
#specs=$(find * -name swagger.json)
#popd
#
#for spec in $specs; do
#  if [[ "$spec" =~ /v[0-9]+((alpha|beta)[0-9]+)?/ ]]; then
#    api=${spec//\/swagger.json/}
#    sanitized=${api//\//_}
#    outdir=generated/${sanitized}
#
#    mkdir -p "${outdir}"
#
#    if [ ! -e "lib_openshift/${sanitized}" ]; then
#      pushd lib_openshift
#      ln -s ../generated/${sanitized}/${sanitized}
#      popd
#    fi
#
#    echo "{ \"packageName\": \"${sanitized}\", \"packageVersion\": \"${PACKAGE_VERSION}\" }" > ${outdir}/swagger_codegen_config.json
#    echo -e "README.md\ntox.ini\n.gitignore\n.travis.yml\ngit_push.sh" > ${outdir}/.swagger-codegen-ignore
#    java -jar ~/bin/swagger-codegen-cli.jar generate -o ${outdir} -i swaggerfiles/${spec} -l python -c ${outdir}/swagger_codegen_config.json -t codegen_templates/individual_api
#  fi
#done
#

echo "{ \"packageName\": \"lib_openshift\", \"packageVersion\": \"${PACKAGE_VERSION}\" }" > swagger_codegen_config.json
java -DdebugModels=true -jar ~/bin/swagger-codegen-cli.jar generate -i swaggerfiles/swagger.json -l python -c swagger_codegen_config.json -t codegen_templates  --git-repo-id lib_openshift --git-user-id ftl-toolbox

sed -i -e 's/self.verify_ssl = True/self.verify_ssl = False/' lib_openshift/configuration.py
