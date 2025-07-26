---
title: "Playwright for Power Platform DevOps Extension"
description: "Automate end-to-end testing for Power Platform apps using Playwright in Azure DevOps pipelines. Zero-config setup, advanced reporting, and multi-browser support."
date: 2025-07-02
categories: ["Pipeline Tools", "Testing", "Power Platform", "DevOps"]
draft: false
sidebar:
  open: true
aliases:
  - /pipeline-tools/playwright-for-power-platform/
---

# Playwright for Power Platform DevOps Extension

Automate end-to-end testing for Power Platform apps using Playwright in Azure DevOps pipelines. This extension provides a seamless setup, robust test execution, and advanced reporting for Power Platform solutions.

{{< youtube IKgxUOEDFog >}}

For a detailed walkthrough and additional insights, check out this comprehensive blog post: [Running Playwright Tests in Azure DevOps for Power Platform](https://techtweedie.github.io/posts/250702-running-playwright-tests-in-azure-devops-for-power-platform/) which covers the complete setup process and best practices.

## Prerequisites

- Windows-based Azure DevOps pipeline agent (Linux/macOS not supported)
- Power Platform application URL
- Test user credentials with permissions
- Playwright test files (JavaScript/TypeScript)

## Obtaining Credentials

- Ensure you have valid Office 365 credentials for authentication.
- Test user credentials should have appropriate permissions for the Power Platform app.

## Supported Operations

- Automated UI testing for Power Platform apps
- Office 365 authentication flows
- Multi-browser testing (Chromium, Firefox, WebKit)
- Advanced reporting (HTML, JSON, JUnit XML)
- Failure analysis (screenshots, video, trace, network logs)
- Power Platform-specific selectors and waits

## Parameters

- **testLocation**: Path to the test files.
- **browser**: Browser to use (e.g., Chromium, Firefox, WebKit).
- **trace**: Trace options (e.g., retain-on-failure).
- **outputLocation**: Directory for test results.
- **appUrl**: URL of the Power Platform app.
- **appName**: Name of the app under test.
- **o365Username**: Office 365 username for authentication.
- **o365Password**: Office 365 password for authentication.

## Using the Connector

### Example Pipeline YAML

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

## Try it Out

- Use the provided YAML snippet to set up your pipeline.
- Run the pipeline and review the generated reports and artifacts.

## Known Issues and Limitations

- Only supports Windows-based Azure DevOps pipeline agents.
- Requires valid Office 365 credentials.

## License

This project is distributed under the MIT License. See the LICENSE file for more details.

## Contributions

Contributions are welcome! Please submit issues or pull requests via the [GitHub repository](https://github.com/mightora/mightora.io).

## Git Repository Contents

- **Source Code**: Contains the implementation of the Playwright for Power Platform extension.
- **Documentation**: Includes guides and examples for using the extension.
- **Tests**: Contains test cases and examples for validation.

## Additional Notes

- Ensure all required parameters are set in the pipeline YAML.
- Review the troubleshooting section for common issues and solutions.

> **Note:** This extension requires Windows-based Azure DevOps pipeline agents.
