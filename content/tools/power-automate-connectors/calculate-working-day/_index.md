---
title: Calculate Working Day
type: docs
weight: 1
sidebar:
  open: false
aliases:
  - /calculate-working-day/
  - /power-automate-connectors/calculate-working-day/
---

## Introduction

The Calculate Working Day API is a tool for developers to easily compute a valid working day, accommodating a range of requirements from basic to complex scenarios. It seamlessly integrates with user-defined working days and UK bank holidays and can perform a number of functions. With a more advanced setup, developers can tailor the computation to adhere to specific working day patterns. By supplying a customized list of working days—designated by their corresponding day-of-week codes—the API can precisely determine the subsequent working day, considering the user-defined schedule.

In addition to the documentation on this site, please feel free to explore the Microsoft Learn Documentation [here](https://learn.microsoft.com/en-us/connectors/calculateworkingday/).

## Prerequisites

To use this connector you will need the following to proceed:
* A Microsoft Power Apps or Power Automate plan

> You need access to premium connectors.

## Obtaining Credentials

It is free to use this connector, and no registration is required.

We are removing references to API Keys in our connector; however, if asked to enter an API key, please enter `free` and if asked for an endpoint, select `RapidAPI`.

## Supported Operations

### Combined
Performs a combination of all of the endpoints in one response.

### Basic Next Working Day
Finds the next working day based on a working week of Monday to Friday.

### Date Difference Calculator
This action uses multiple variables to determine what your working days are between two dates.

### Next Working Day
This action uses multiple variables to determine what your working days are in order to return the correct Next Working Day after the date you provide.

### First and Last Working Day of Month
This action uses multiple variables to determine what your First and Last working days of a given month are.

### Is Today A Working Day
This action uses multiple variables to determine if today/date supplied is a working day for you.

### Date In X Working Days
This action uses multiple variables to determine what the working day will be in X working days’ time.

## Parameters

* __date__ - The date in question you wish to centre your request around. This is the input date in YYYY-MM-DD format. e.g. 2022-12-23.
* __working_days__ - This parameter expects a comma-separated list of working days, where Monday is 1, Tuesday is 2, and so on. In the default, we're using all weekdays from Monday to Friday, so the value is '1,2,3,4,5'.
* __x_working_days__ - Find working day in X days e.g. 4
* __country__ - Currently, only the United Kingdom is supported. Values can be england-and-wales, scotland, northern-ireland. Used to filter out bank holidays.
* __non_working_days__ - A custom list of non-working days, this could be a list of days where service is not available. In a string as a list, format YYYY-MM-DD,YYYY-MM-DD e.g. 2022-12-28,2022-12-29,2022-12-30.

## Using the Connector

To use our connector:
1. Add it into your Power Automate Flow.
2. We are removing references to API Keys in our connector; however, if asked to enter an API key, please enter `free` and if asked for an endpoint, select `RapidAPI`.
3. Choose your action.
4. Pass in the optional and required parameters depending on the action.

## Try it Out

{{< callout type="info" >}}
    We are removing references to API Keys in our connector; however, if asked to enter an API key, please enter `free` and if asked for an endpoint, select `RapidAPI`.
{{< /callout >}}

{{< swagger-client "https://raw.githubusercontent.com/mightora/customConnectors/main/calculateWorkingDay/apiDefinition.swagger.json" >}}

## Known Issues and Limitations

* Currently, there are no known issues.

## License

This project is distributed under the MIT License. This license allows for personal and commercial use, modification, distribution, and private use.

## Contributions

We welcome contributions to this project. Please visit our [GitHub repository](https://github.com/mightora/customConnectors) for more information and instructions on submitting issues or pull requests.

## Git Repository Contents

The repository contains the following:
* **Swagger Definition**: The API definition for the connector.
* **Source Code**: The implementation of the connector.
* **Documentation**: Guides and instructions for using the connector.
* **Tests**: Test cases and examples for validating the connector.

## Additional Notes

* Avoid repetitive content.
* Fix any typos or grammatical errors.
* Ensure the document flows logically and is easy to follow.
* Use consistent formatting for headings, lists, and code snippets.