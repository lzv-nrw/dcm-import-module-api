# Digital Curation Manager - Import Module API

The 'DCM Import Module'-API provides functionality to import
* Intellectual Entities (IEs) from a remote system and
* pre-built Information Packages (IPs) from the internal storage.

This repository contains the corresponding OpenAPI-document.
For the associated implementation, please refer to the sibling package [`dcm-import-module`](https://github.com/lzv-nrw/dcm-import-module).

The contents of this repository are part of the [`Digital Curation Manager`](https://github.com/lzv-nrw/digital-curation-manager).

## Building an SDK-package
Some dcm-applications rely on pre-built sdk-packages, i.e., python clients for specific APIs.

Consider using the corresponding packages available via the extra-index-url `https://zivgitlab.uni-muenster.de/api/v4/projects/9020/packages/pypi/simple`.
In order to manually build these packages, perform the following actions:

1. Get the OpenAPI Generator-archive, e.g., by running
   ```
   wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.5.0/openapi-generator-cli-7.5.0.jar -O openapi-generator-cli.jar
   ```
1. Create a JSON-file `config.json` with the package information
   ```json
   {
     "packageName": "dcm_import_module_sdk",
     "projectName": "dcm-import-module-sdk",
     "packageVersion": "<VERSION>"
   }
   ```
1. Run the generator
   ```
   java -jar ../openapi-generator-cli.jar generate -i dcm_import_module_api/openapi.yaml -g python -o sdk -c config.json
   ```

# Contributors
* Sven Haubold
* Orestis Kazasidis
* Stephan Lenartz
* Kayhan Ogan
* Michael Rahier
* Steffen Richters-Finger
* Malte Windrath
* Roman Kudinov