---
title: Send Email with Graph
type: docs
weight: 1
prev: /power-automate-connectors/send-email-with-graph/
next: /power-automate-connectors/send-email-with-graph/gettingstarted/
sidebar:
  open: true
aliases:
  - /power-automate-connectors/send-email-with-graph/
---

## Introduction

The **Send Email with Graph** connector leverages **Microsoft Graph** to enable seamless email sending capabilities within Power Automate. This connector allows you to send emails from **Power Automate** without the need to create a **User Account** from your Microsoft 365 organization, ensuring secure and efficient communication.

It supports **HTML text formatting, attachments, To, CC, BCC,** making it a versatile tool for sending emails from Power Automate.

For a full guide on how to install it, check out the [blog post here](https://techtweedie.github.io/posts/send-emails-from-flow-without-a-service-account/).

## Prerequisites

To use this connector, you will need:

- Access to Microsoft 365.
- Permissions to create an app registration in Entra.
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
4. Search for **mail.send**, open the **Mail** option, and select **mail.send**.

> **Note:** This permission allows sending emails as anyone. Restrict access appropriately.

### Step 4 - Grant Admin Consent

1. Ask a Global Administrator to grant admin consent for the app registration.

## Supported Operations

The connector supports the following operations:

- Sending emails with HTML formatting.
- Adding attachments to emails.
- Using To, CC, and BCC fields.

## Parameters

Below are the parameters required for the connector:

- **user-email**: The email address of the sender.
- **message.subject**: The subject of the email.
- **message.body.contentType**: The content type (e.g., HTML).
- **message.body.content**: The body of the email.
- **saveToSentItems**: Boolean to save the email in Sent Items.
- **emailAddress.address**: The recipient's email address.

## Using the Connector

### Step 1 - Find custom connectors

1. Navigate to `https://make.powerautomate.com/`.
2. Change your environment if needed.
3. In the left-hand menu, navigate to **More** > **Discover all** > **Custom connectors**.

### Step 2 - Create a new connector

1. Click on **New custom connector**.
2. Select **Import an OpenAPI from URL**.
3. Enter the connector name `Send email using Graph`.
4. Provide the URL: `https://raw.githubusercontent.com/itweedie/PowerPlatform-Send-Emails-from-Power-Automate-without-a-Service-Account/refs/heads/main/connector/shared_mightora-5fsend-20mail-20with-20graph-5fe07b0f04a8b0d4c3/apiDefinition.swagger.json`.

### Step 3 - Configure your connector

1. Go to the **Security** tab.
2. Set **OAuth 2.0** as the authentication type.
3. Set the Identity Provider to **Azure Active Directory** and enable **Service Principle support**.
4. Enter the **Client ID** and **Secret Value** from your app registration.

### Step 4 - Add C# to process attachments (Optional)

If you need to send attachments, add the provided C# code to the connector's code section.

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

Contributions are welcome! Please submit issues or pull requests via the [GitHub repository](https://github.com/itweedie/PowerPlatform-Send-Emails-from-Power-Automate-without-a-Service-Account).

## Git Repository Contents

- **Swagger Definition**: API definition for the connector.
- **Source Code**: C# code for processing attachments.
- **Documentation**: Instructions for using the connector.
- **Tests**: Example test cases.

## Additional Notes

- Avoid repetitive content.
- Ensure the document flows logically and is easy to follow.
- Use consistent formatting for headings, lists, and code snippets.
