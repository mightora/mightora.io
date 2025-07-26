---
title: "Getting Started"
description: "How to set up and use the Playwright for Power Platform DevOps extension in Azure DevOps pipelines."
date: 2025-07-02
categories: ["Pipeline Tools", "Testing", "Power Platform", "DevOps"]
draft: false
type: docs
---

## Getting started 

{{< youtube IKgxUOEDFog >}}

For a detailed walkthrough and additional insights, check out this comprehensive blog post: [Running Playwright Tests in Azure DevOps for Power Platform](https://techtweedie.github.io/posts/250702-running-playwright-tests-in-azure-devops-for-power-platform/) which covers the complete setup process and best practices.

## Prerequisites

- Windows-based Azure DevOps pipeline agent
- Power Platform app URL
- Test user credentials
- Playwright test files (JavaScript/TypeScript)

## Installation Steps

1. Install the extension in your Azure DevOps organization
2. Add the Playwright for Power Platform task to your pipeline
3. Configure required parameters (test location, browser, app URL, credentials)

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
