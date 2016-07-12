## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

To use the bindings, import the pacakge:

```python
import lib_openshift
```

## Some basic info

OpenShift v1 api is exposed via lib_openshift.OapivApi
Kubernetes v1 api is exposed via lib_openshift.ApivApi

Autoscaling v1 api is exposed via lib_openshift.ApiautoscalingvApi
Batch v1 api is exposed via lib_openshift.ApibatchvApi
Extensions v1beta1 api is exposed via lib_openshift.ApiextensionsvbetaApi

models are exposed directly under lib_openshift

## Simple test script

```
import lib_openshift
import urllib3

urllib3.disable_warnings()

my_endpoint = 'https://109.0.0.51:8443'
my_token = 'Bearer vyXQ_ISfV8JeZeMhvd81Dqxb45KHRZMT8Xf3XLJvfUY'

client = lib_openshift.ApiClient(my_endpoint, 'Authorization', my_token))

apiv1=lib_openshift.ApivApi(client)
oapiv1=lib_openshift.OapivApi(client)

oapiv1.list_namespaced_project()
```

## Generating Docs from virtualenv

pip install -r docs_requirements.txt
make -C docs html SPHINXBUILD="python $(which sphinx-build)"
xdg-open docs/_build/html/index.html

## Getting Started

TODO


## Documentation

TODO
