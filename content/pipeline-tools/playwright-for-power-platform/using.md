---
title: "Using Playwright for Power Platform"
description: "How to use the Playwright for Power Platform DevOps extension, with test examples and troubleshooting tips."
date: 2025-07-02
categories: ["Pipeline Tools", "Testing", "Power Platform", "DevOps"]
draft: false
---
# Using Playwright for Power Platform

## Common Test Scenarios

### Authentication Testing
```javascript
test('Office 365 Login Flow', async ({ page }) => {
  await page.goto(process.env.APP_URL);
  await page.fill('[name="loginfmt"]', process.env.O365_USERNAME);
  await page.click('[type="submit"]');
  await page.fill('[name="passwd"]', process.env.O365_PASSWORD);
  await page.click('[type="submit"]');
  await expect(page).toHaveTitle(new RegExp(process.env.APP_NAME));
});
```

### Canvas App Testing
```javascript
test('Form Submission Workflow', async ({ page }) => {
  await page.goto(process.env.APP_URL);
  await page.waitForSelector('[data-automation-id="Canvas"]');
  await page.click('[aria-label="Name input"]');
  await page.fill('[aria-label="Name input"]', 'Test User');
  await page.click('[aria-label="Submit button"]');
  await expect(page.locator('[aria-label="Success message"]')).toBeVisible();
});
```

## Troubleshooting
- Check credentials and permissions for authentication issues
- Add waits for slow-loading elements
- Review HTML reports and trace files for debugging
