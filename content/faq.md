---
title: Frequently Asked Questions
type: docs
toc: true
---


Get quick answers to common questions about Mightora tools and Power Platform automation.

## 🔧 Getting Started

### How do I start using Mightora connectors?

1. **Browse the catalogue** in [All Mightora tools](/tools/)
2. **Explore browser apps** from the [tool directory](/tools/)
3. **Follow the setup guides** for each connector
4. **Check the project repository** for maintenance information and issues

### Are the connectors really free?

Mightora lists tools that are free to explore. A specific tool may depend on Microsoft licences, external APIs or other services that carry their own conditions or costs. Check the tool's documentation and the licence of its source repository before deploying or modifying it.

### Do I need any special permissions or licenses?

Most connectors work with standard Power Platform licenses. Specific requirements are listed in each connector's documentation. Generally, you'll need:

- Power Automate license (included in most Microsoft 365 plans)
- Appropriate permissions for your target systems
- Basic Power Platform development access

## 🛠️ Technical Questions

### What's the difference between connectors and pipeline tools?

**Connectors** are used within Power Automate flows for real-time automation:
- Calculate Working Day
- Email Domain Checker  
- Send Email with Graph

**Pipeline Tools** are for DevOps and deployment automation:
- Dataverse 4 Teams Tools
- Power Platform DevOps Extension
- Playwright for Power Platform

### How reliable are the APIs?

Availability and support arrangements differ between projects. We do not publish a universal uptime guarantee for all Mightora tools. You can consult the [public service status page](https://stats.uptimerobot.com/3EPW8gBu4N), bearing in mind that monitoring does not guarantee future availability.

### Can I use these in production environments?

Evaluate the particular connector or application for your organisation's requirements, including its source, access permissions, dependencies, handling of sensitive information, resilience and licensing. Examples and community tooling do not constitute an independent security certification.

### What about rate limits?

Limits depend on the individual tool and any downstream platform or API it calls. The catalogue does not assert numerical limits for services that have not been independently verified. Consult current Microsoft and tool-specific documentation before building a production dependency.

## 🔒 Security & Privacy

### How secure are your connectors?

Security characteristics differ by project and deployment. Inspect the code, required credentials, permissions, external dependencies and relevant GitHub checks before entering sensitive data. A passing CI or CodeQL badge is not a guarantee of security.

### What data do you collect?

The main Mightora website uses analytics and other third-party resources; see the [privacy policy](/privacy/) for the published policy. Individual applications may have different data flows and operators. Check each application's own network activity, documentation and privacy statement rather than assuming that all data stays in your browser.

## 🚀 Advanced Usage

### Can I modify or extend the connectors?

Many Mightora projects make their source available in the [Mightora GitHub organisation](https://github.com/mightora). Reuse rights are governed by each project's actual licence. Review the licence file and contribution guidance before redistributing or extending a project.

### Do you offer enterprise support?

Commercial support is not implied by the free tools catalogue. For enquiries about consulting or custom development, use the published [contact website](https://iantweedie.biz), without assuming a support contract exists.

### How do I report bugs or request features?

We welcome feedback! You can:
- Report issues on [GitHub](https://github.com/mightora)
- Review the project's GitHub issues and discussions, if enabled
- Email us directly through our [Contact page](https://iantweedie.biz)

## 📚 Learning Resources

### Where can I find tutorials?

Check out these learning resources:
- [All Mightora tools](/tools/)
- [TechTweedie blog](https://techtweedie.github.io) for detailed tutorials
- YouTube videos embedded in each connector's documentation
- [Community examples](/community/) from other users

### Do you offer training?

We provide various training options:
- Free documentation and tutorials
- Individual open-source project documentation
- Third-party/vendor training, where available
- Contact for separate consulting enquiries

## 💡 Still Have Questions?

Can't find what you're looking for? We're here to help!

{{< cards >}}
  {{< card link="https://github.com/mightora" title="GitHub Projects" icon="github" >}}
  {{< card link="https://github.com/mightora" title="GitHub Discussions" icon="github" >}}
  {{< card link="https://iantweedie.biz" title="Direct Contact" icon="email-at" >}}
{{< /cards >}}

---

*Last reviewed: 19 October 2026. Verify individual project capabilities and privacy details before use.*
