---
title: SharePoint with Graph Connector
type: docs
weight: 1
sidebar:
  open: true
---

## Introduction

The **SharePoint with Graph** connector leverages **Microsoft Graph** to enable seamless permission management capabilities within Power Automate. This connector allows you to grant and remove item or folder permissions in **SharePoint** using a **Service Principal**, ensuring secure and efficient access control.

It supports **granular permission settings, site-specific access, and integration with Power Automate**, making it a versatile tool for managing SharePoint permissions.

For a full guide on how to install it, check out the [blog post here](https://techtweedie.github.io/posts/250217-set-folder-permissions-in-sharepoint-with-power-automate-flow/#download-and-testing-the-connector).

## Prerequisites

To use this connector, you will need:

- Access to Microsoft 365.
- Permissions to create an app registration in Entra.
- Ownership of the SharePoint site where permissions will be managed.
- A Power Automate environment.

## Obtaining Credentials

To use this connector, you will need to create an application registration.

### Step 1 - Log in to Entra

1. Go to [https://entra.microsoft.com](https://entra.microsoft.com) and log in with your user account.

### Step 2 - Create the app registration

1. On the Entra Overview page, open **Identity**.
2. Navigate to **Applications** in the left-hand menu and open **App Registrations**.
3. Select **New Registration**.
4. Provide a name for your app registration and click **Next**.

### Step 3 - Add API permission

1. In the left-hand menu, click on **API Permission**.
2. Click on **Add permission**.
3. Select **Application Permission**.
4. Search for **sites.selected**, open the **Sites** option, and select **sites.selected**.

> **Note:** This permission allows access to specific SharePoint sites. Restrict access appropriately.

### Step 4 - Grant Admin Consent

1. Ask a Global Administrator to grant admin consent for the app registration.

## Supported Operations

The connector supports the following operations:

- Granting permissions to SharePoint items or folders.
- Removing permissions from SharePoint items or folders.
- Listing drives and folders within a SharePoint site.

## Parameters

Below are the parameters required for the connector:

- **siteID**: The ID of the SharePoint site.
- **driveID**: The ID of the document library.
- **itemID**: The ID of the item or folder.
- **roles**: The permission roles to assign (e.g., read, write).
- **email**: The email address of the user to grant permissions to.

## Using the Connector

### Step 1 - Find custom connectors

1. Navigate to `https://make.powerautomate.com/`.
2. Change your environment if needed.
3. In the left-hand menu, navigate to **More** > **Discover all** > **Custom connectors**.

### Step 2 - Create a new connector

1. Click on **New custom connector**.
2. Select **Import an OpenAPI from URL**.
3. Enter the connector name `SharePoint with Graph`.
4. Provide the URL: `https://raw.githubusercontent.com/itweedie/PowerPlatform-PowerAutomate-SharePoint-with-Graph-Connector/refs/heads/main/connector/shared_sharepoint-20with-20graph-5fbb1338f75d4745cb-5f8d99aea54e2a1a34/apiDefinition.swagger.json`.

### Step 3 - Configure your connector

1. Go to the **Security** tab.
2. Set **OAuth 2.0** as the authentication type.
3. Set the Identity Provider to **Azure Active Directory** and enable **Service Principal support**.
4. Enter the **Client ID** and **Secret Value** from your app registration.

## Try it Out

### Step 1 - Add your first connection

1. Go to the **Test** tab.
2. Click on **New connection**.
3. Enter your **Secret**, **Client ID**, and **Tenant ID**.
4. Click **Create Connection**.

### Step 2 - Test the connector

1. Scroll to **Operations**.
2. Fill in the required parameters.
3. Click **Test operation** and verify the response.

## Known Issues and Limitations

- Requires Global Admin consent for API permissions.
- Limited to the permissions granted during app registration.

## License

This project is distributed under the MIT License. See the LICENSE file for more details.

## Contributions

Contributions are welcome! Please submit issues or pull requests via the [GitHub repository](https://github.com/itweedie/PowerPlatform-PowerAutomate-SharePoint-with-Graph-Connector).

## Git Repository Contents

- **Swagger Definition**: API definition for the connector.
- **Source Code**: Example code for managing permissions.
- **Documentation**: Instructions for using the connector.
- **Tests**: Example test cases.

## Additional Notes

- Avoid repetitive content.
- Ensure the document flows logically and is easy to follow.
- Use consistent formatting for headings, lists, and code snippets.
