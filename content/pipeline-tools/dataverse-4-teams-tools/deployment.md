---
title: Deployment Instructions
type: docs
weight: 8
---
To deploy the Power Platform Dataverse 4 Teams Scripts, follow these steps:

## Option 1 
Use https://github.com/mightora/Power-Paltform-Dataverse4Teams-Tools as a template for your own repository 

## Option 2
Clone the repository to your local machine 

## Option 3
Add it as a submodule to an existing project.
```bash
git submodule add https://github.com/mightora/Power-Platform-Dataverse4Teams-Tools.git dataverse4TeamsTools
git submodule update --init --recursive
```

## Then
Open the project in your preferred IDE (e.g., Visual Studio Code).
Set up your environment by ensuring you have the necessary tools like PowerShell and Git installed.
Run the provided PowerShell scripts for exporting and importing solutions between environments.

