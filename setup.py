import os
from setuptools import setup

setup(
    version="5.2.1",
    name="dcm-import-module-api",
    description="specification of the DCM Import Module API",
    author="LZV.nrw",
    license="MIT",
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
