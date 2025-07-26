---
title: "Using Playwright"
description: "How to use the Playwright for Power Platform DevOps extension, with test examples and troubleshooting tips."
date: 2025-07-02
categories: ["Pipeline Tools", "Testing", "Power Platform", "DevOps"]
draft: false
type: docs
---



## Example Pipeline YAML

```yaml
pool:
  vmImage: 'windows-latest'

steps:
- task: mightoria-playwrightForPowerPlatform@1
  displayName: 'Run Power Platform Tests'
  inputs:
    testLocation: '$(System.DefaultWorkingDirectory)/tests'
    browser: 'chromium'
    trace: 'retain-on-failure'
    outputLocation: '$(Agent.TempDirectory)/test-results'
    appUrl: 'https://apps.powerapps.com/play/$(AppId)'
    appName: 'MyPowerApp'
    o365Username: '$(TestUser.Email)'
    o365Password: '$(TestUser.Password)'
```


## Troubleshooting
- Check credentials and permissions for authentication issues
- Add waits for slow-loading elements
- Review HTML reports and trace files for debugging
