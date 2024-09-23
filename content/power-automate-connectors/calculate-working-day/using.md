---
title: Using the connector
type: docs
weight: 7
---
To use our connector;
1. Add it in to your Power Automate Flow.
2. If asked for API key please enter `free` and if asked for endpoint select `RapidAPI`.
3. Choose your action
4. Pass in the optional and required parameters depending on the action. 
## Parameters that can be used
* __date__ - The date in question you wish to centre your request around. This is the input date in YYYY-MM-DD format. e.g. 2022-12-23.
* __working_days__ - This parameter expects a comma-separated list of working days, where Monday is 1, Tuesday is 2, and so on. In the default, we're using all weekdays from Monday to Friday, so the value is '1,2,3,4,5'.
* __x_working_days__ - Find working day in X days e.g. 4
* __country__ - Currently, only the United Kingdom is supported. Values can be england-and-wales, scotland, northern-ireland. Used to filter out bank holidays.
* __non_working_days__ - A custom list of non working days, this could be a list of days where service is not available. In a string as a list, format YYYY-MM-DD,YYYY-MM-DD e.g. 2022-12-28,2022-12-29,2022-12-30.