# Changelog

## [6.2.0] - 2025-08-20

### Added

- added optional submission token

## [6.1.0] - 2025-07-25

### Added

- added test-configuration to GET-/identify response
- added test-import mode to POST-/import/internal

## [6.0.0] - 2025-02-14

### Changed

- **Breaking:** replaced connected services-API-related blocks in request bodies with free-form objects (individual blocks for calls to Object Validator and IP Builder)

## [5.2.1] - 2024-11-21

### Changed

- updated package metadata and README

## [5.2.0] - 2024-10-11

### Added

- added /import-DELETE endpoint for abort mechanism

## [5.1.3] - 2024-09-11

### Fixed

- fixed required-flag for field 'logId' in `IP` (`6caf6293`)

## [5.1.2] - 2024-09-10

### Fixed

- fixed required-flag for field 'IPs' in `JobData` (`2b3571f5`)
- fixed required-flag for field 'valid' in `IP` (`d1e19b1f`)

## [5.1.0] - 2024-09-06

### Changed

- **Breaking:** changed path of `/import` to `/import/external` (`e154ca39`)
- **Breaking:** update SelfDescription for scalable orchestration (`a67f9f12`)
- **Breaking:** rename JobToken field 'token' to 'value' (`e7b5c92f`)

### Added

- added endpoint `/import/internal` for import from hotfolder (`e154ca39`)

## [4.0.0] - 2024-07-17

### Changed

- **Breaking:** refactored /identify-GET response to common DCM-format (`315fcdb1`)
- **Breaking:** removed requirement for `JobData.success` (`7af4add1`)

## [3.0.0] - 2024-01-25

### Changed

- renamed schema `DateTime` to `ISODateTime` (reserved by swagger codegen) (`e2bb0ec0`)
- **Breaking:** improved Report schema, now supports custom job output data format and Reports of child processes (`0f1a57d1`)
- **Breaking:** changed requestBody format (`870e7110`)
- removed placeholder data-block from Report schema (`620fb127`)
- replaced current logID by the reference to the ReportIdentifier schema (`314a6216`)
- made "build"-block in import request optional (`5c2758c8`)
- **Breaking:** migrated to OpenAPI-generator for SDK generation (`35defe56`)

## [2.0.3] - 2024-02-21

### Fixed

- marked ip_builder_host in SelfDescription as required property (`2a98f68f`)
- fixed example of plugin schema's signature (`922e2567`)
- updated description of bagit profiles (`83e71b4f`)

## [2.0.0] - 2024-02-15

### Changed

- **Breaking:** generalized Report schema by generic categories (`c2c07a03`)

### Added

- added description and example to ImportArgSignature properties (`eeb2cb54`)

### Removed

- removed unneeded default value type for plugin signature arguments (`3fb18ef9`)

### Fixed

- added `format: base64` to `BuildConfig` as serialized object schema (`c5fa469f`)
- fixed error in plugin signature schema not being fully recursive (`b8342604`)

## [1.1.0] - 2024-02-09

### Added

- added support of nested plugin signatures (`a6bea86b`)

## [1.0.0] - 2024-02-02

### Changed

- **Breaking:** changed ImportConfig.args format to arbitrary object (instead of list of objects) (`567e83b8`)
- **Breaking:** changed operationId of /import-POST to `import_ips` (`4797b271`)

### Fixed

- make Plugin-Dependencies properties name and version required (`cedefa4c`)

## [0.1.0] - 2024-01-30

### Changed

- initial release of dcm-import-module-api
