import os
from setuptools import setup

setup(
    version="5.2.0",
    name="dcm-import-module-api",
    description="api for import-module-containers",
    author="LZV.nrw",
    install_requires=[
    ],
    packages=[
        "dcm_import_module_api",
    ],
    package_data={
        "dcm_import_module_api": [
            "dcm_import_module_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
