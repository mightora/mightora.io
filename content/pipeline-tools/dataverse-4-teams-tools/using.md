---
title: Using the script
type: docs
weight: 7
---


## Download From Source

This script exports a solution from a source environment, generates a solution settings template, and unpacks the solution, including any Canvas Apps it contains.

### Parameters:

- `-solutionName`: The name of the solution to export.
- `-exportDirectory`: Directory where the solution's zip file will be exported.
- `-sourceEnv`: ID of the source environment from which to export the solution.
- `-unpackDirectory`: Directory where the solution will be unpacked and Canvas Apps will be processed.

### Example Usage:

```powershell
.\pipelineScripts\downloadFromSource.ps1 -solutionName "Dataverse4TeamsDemo" -exportDirectory ".\demo\dataverse4TeamsDemo" -sourceEnv "1838fca4-6258-e6b8-a710-60838df81aa3" -unpackDirectory ".\demo\dataverse4TeamsDemo\unpacked"
```


## Release to Target

This script re-packs a previously unpacked solution and imports it into a target environment. If an environment settings file is provided, the import will include those settings.

### Parameters:

- `-solutionName`: Name of the solution to be processed.
- `-unpackDirectory`: Directory where the solution is unpacked.
- `-environmentSettingsFile`: (Optional) Path to the environment settings file.
- `-targetEnvironment`: Target environment to which the solution will be imported.
- `-exportDirectory`: Directory where the repacked solution will be exported.
- `-Managed`: Switch to indicate whether the solution should be managed.

### Example Usage:

**With a settings file:**

```powershell
.\pipelineScripts\releaseToTarget.ps1 -solutionName "Dataverse4TeamsDemo" -unpackDirectory ".\demo\dataverse4TeamsDemo\unpacked" -exportDirectory ".\demo\dataverse4TeamsDemo" -environmentSettingsFile ".\demo\settings.json" -targetEnvironment "5fc7b0a0-dc6e-e682-8886-bad6dac246a7"
```

**As Managed:**

```powershell
.\pipelineScripts\releaseToTarget.ps1 -solutionName "Dataverse4TeamsDemo" -unpackDirectory ".\demo\dataverse4TeamsDemo\unpacked" -exportDirectory ".\demo\dataverse4TeamsDemo" -environmentSettingsFile ".\demo\settings.json" -targetEnvironment "5fc7b0a0-dc6e-e682-8886-bad6dac246a7" -managed
```

**Without a settings file:**

```powershell
.\pipelineScripts\releaseToTarget.ps1 -solutionName "Dataverse4TeamsDemo" -unpackDirectory ".\demo\dataverse4TeamsDemo\unpacked" -exportDirectory ".\demo\dataverse4TeamsDemo" -targetEnvironment "5fc7b0a0-dc6e-e682-8886-bad6dac246a7"
```