---
title: Supported Operations
type: docs
weight: 4
---

### Send Email

The "Send Email" operation allows for sending an email from a specified user account using the Microsoft Graph API. Below are the details and parameters required for this operation:

#### Parameters:


- **User-email (string, required):** The email address of the user sending the email.
- **Message (object, required):** The email message details.
  - **Subject (string, required):** The subject of the email.
  - **Body (object, required):** The body of the email.
    - **Content Type (string, required):** The content type of the body. Possible values are Text or HTML.
    - **Content (string, required):** The content of the email body.
  - **ToRecipients (array, required):** The list of recipients to whom the email is sent.
    - **EmailAddress (object, required):** The email address of the recipient.
      - **Address (string, required):** The email address.
  - **CcRecipients (array, optional):** The list of recipients to be CC'd.
    - **EmailAddress (object, required):** The email address of the recipient.
      - **Address (string, required):** The email address.
  - **BccRecipients (array, optional):** The list of recipients to be BCC'd.
    - **EmailAddress (object, required):** The email address of the recipient.
      - **Address (string, required):** The email address.
  - **Attachments (array, optional):** The list of attachments.
    - **Name (string, required):** The name of the attachment.
    - **ContentBytes (string, required):** The content of the attachment in base64 format.
- **SaveToSentItems (boolean, optional):** Indicates whether to save the email to the Sent Items folder. Default is true.