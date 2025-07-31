---
title: Power Platform Solution Modifier
type: docs
weight: 1
sidebar:
  open: true

---


The Mightora Power Platform Solution Modifier is a specialized Azure DevOps extension designed to programmatically modify Power Platform solution XML files during CI/CD pipelines. This extension provides two powerful tasks - **XML Node Updater** and **XML Node Attribute Updater** - that allow advanced users to dynamically edit solution configurations within release and build pipelines without manual intervention. 

**Created by:**

[![Mightora Logo](https://raw.githubusercontent.com/TechTweedie/techtweedie.github.io/main/static/logo-01_150x150.png)](https://techtweedie.github.io)


# Setup 
- Install the Solution Modifier extension in your DevOps Organization using the **Get it free** button.
- Navigate to your pipeline.
- Add the XML modification tasks to your pipeline.
- Configure the tasks with appropriate XML file paths and XPath expressions.

# Support
Please visit [mightora.io](https://mightora.io)

# Key Features 

This extension provides two essential tasks for modifying Power Platform solution XML files during your CI/CD pipeline execution. 

## Solution XML Node Attribute Updater

### Overview
This task updates specific attributes in XML solution files using PowerShell, allowing dynamic adjustments without manual editing during your CI/CD pipeline execution.

### Key Features
- **Automated XML Attribute Updates**: Modifies XML attribute values during pipeline execution
- **XPath Node Selection**: Uses XPath expressions to precisely select specific XML nodes
- **Flexible Configuration**: Configure file paths, node XPath expressions, attribute names, and new values
- **CI/CD Integration**: Perfect for automating configuration changes, version updates, and environment-specific modifications
- **PowerShell-Based**: Reliable XML processing using PowerShell's built-in XML capabilities

### How to Use
1. Add the task to your Azure DevOps pipeline
2. Configure the required inputs:
    - `XmlFilePath`: Path to the XML file to modify
    - `NodeXPath`: XPath expression to locate the target XML node
    - `attributeName`: Name of the attribute to modify
    - `NewValue`: New value for the attribute
3. Run the pipeline to update the XML file

### Example Pipeline Usage

```yaml
- task: solutionXMLNodeAttributeUpdater@1
  inputs:
    xmlFilePath: "$(Build.SourcesDirectory)/Solutions/MySolution/Entity.xml"
    nodeXPath: "/Entity/Attributes/Attribute[@Name='DisplayName']"
    attributeName: "DisplayName"
    newValue: "NewDisplayName"
```

### Use Cases
- Update solution version numbers
- Modify display names for different environments
- Change configuration settings based on deployment target
- Update connection references for different environments

## Solution XML Node Updater

### Overview
This task updates the inner text content of specific XML nodes within Power Platform solution files, enabling dynamic content modifications during pipeline execution.

### Key Features
- **Automated Node Content Updates**: Modifies XML node values during pipeline execution
- **Precise Node Selection**: Uses XPath expressions to locate and modify specific nodes
- **Dynamic Content Management**: Allows runtime updates to XML node content
- **Pipeline Integration**: Seamlessly integrates into build and release pipelines
- **PowerShell-Based**: Robust XML processing using PowerShell's XML manipulation capabilities

### How to Use
1. Add the task to your Azure DevOps pipeline
2. Configure the required inputs:
    - `XmlFilePath`: Path to the XML file containing the node to update
    - `NodeXPath`: XPath expression to locate the target XML node
    - `NewValue`: New content value for the node
3. Run the pipeline to update the XML node content

### Example Pipeline Usage

```yaml
- task: solutionXMLNodeUpdater@1
  inputs:
    xmlFilePath: "$(Build.SourcesDirectory)/Solutions/MySolution/Entity.xml"
    nodeXPath: "/Entity/Attributes/Attribute[@Name='Description']"
    newValue: "Updated description for production environment"
```

### Use Cases
- Update descriptions and help text for different environments
- Modify URLs and connection strings
- Change default values based on deployment context
- Update configuration parameters dynamically

## Common Scenarios

Both tasks are particularly useful for:

- **Environment-Specific Deployments**: Automatically adjust solution configurations for Dev, Test, and Production environments
- **Version Management**: Update version numbers and build information in solution files
- **Configuration Management**: Modify settings, URLs, and parameters without manual intervention
- **Automated Compliance**: Ensure consistent naming conventions and settings across deployments

## Requirements

- Azure DevOps pipeline with access to solution XML files
- Basic understanding of XPath expressions for node selection
- PowerShell execution capability in the pipeline agent