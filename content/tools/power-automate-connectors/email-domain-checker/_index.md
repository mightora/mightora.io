---
title: Email Domain Checker
type: docs
weight: 1
prev: /power-automate-connectors/email-domain-checker/
next: /power-automate-connectors/email-domain-checker/gettingstarted/
sidebar:
  open: false
---

## Introduction

An email domain validator is essential for ensuring valid email addresses and reducing bounce rates, enhancing data quality, and preventing fraud. It helps maintain data accuracy, comply with regulations, and save costs in email communications. Its primary role is to verify the authenticity and correctness of email domains to improve data management and user experience.

In addition to the documentation on this site, please feel free to explore the Microsoft Learn Documentation [here](https://learn.microsoft.com/en-us/connectors/emaildomainchecker/).

## Prerequisites

To use this connector you will need the following to proceed:

* A Microsoft Power Apps or Power Automate plan

## Obtaining Credentials

It is free to use this connector, and no registration is required.

If asked for API key please enter `free` and if asked for endpoint select `RapidAPI`.

## Supported Operations

### Check Domain

Allows for the checking of a domain, verifying its existence and validity.

## Parameters that can be used

* __domain__* - The domain you wish to check.

## Using the connector

To use our connector:

1. Add it into your Power Automate Flow.
2. If asked for API key please enter `free` and if asked for endpoint select `RapidAPI`.
3. Choose your action.
4. Pass in the optional and required parameters depending on the action.

## Try it out

{{< callout type="info" >}}
  If asked for API key please enter `free` and if asked for endpoint select `RapidAPI`.
{{< /callout >}}

{{< swagger-client "https://raw.githubusercontent.com/mightora/customConnectors/main/emailDomainChecker/swagger.json" >}}

## Known Issues and Limitations

* Currently there are no known issues.
* Currently we limit to 1000 calls per minute, we will look to increase this if there is demand.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

## Contributions

This is an open-source project, and contributions are welcome! If you would like to contribute, please visit our GitHub repository:

[GitHub Repository](https://github.com/mightora/customConnectors)

Feel free to submit issues, feature requests, or pull requests to improve the project.

## Git Repository Contents

The GitHub repository contains the following:

- **Swagger Definition**: The OpenAPI specification for the connector.
- **Source Code**: The implementation of the connector.
- **Documentation**: Additional documentation and examples.
- **Tests**: Test cases to validate the functionality of the connector.

Explore the repository to learn more about the project and its structure.
