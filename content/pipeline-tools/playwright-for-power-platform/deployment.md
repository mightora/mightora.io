---
title: "Deployment Guide for Playwright for Power Platform"
description: "How to deploy and configure the Playwright for Power Platform DevOps extension in Azure DevOps pipelines."
date: 2025-07-02
categories: ["Pipeline Tools", "Testing", "Power Platform", "DevOps"]
draft: false
---
# Deployment Guide

## Installing the Extension

1. Go to the Azure DevOps Marketplace
2. Search for "Playwright for Power Platform"
3. Click **Install** and select your organization

## Adding to Your Pipeline

- Use the provided YAML snippet in your pipeline definition
- Ensure all required parameters are set

## Artifacts & Reports

- Test results are published as HTML, JSON, and JUnit XML
- Screenshots and videos are attached to results for analysis
