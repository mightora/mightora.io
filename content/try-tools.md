---
title: Try Our Tools
type: docs
weight: 1
draft: true
---

Test our connectors with live examples before implementing them in your flows!

## Calculate Working Day - Live Demo

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #0078d4;">
    <h3>🔧 Interactive Calculator</h3>
    <p>Try our working day calculation right here:</p>
    
<div style="margin: 15px 0;">
        <label for="startDate" style="display: block; margin-bottom: 5px; font-weight: bold;">Start Date:</label>
        <input type="date" id="startDate" style="padding: 8px; border: 1px solid #ccc; border-radius: 4px; width: 200px;">
    </div>
    
<div style="margin: 15px 0;">
        <label for="daysToAdd" style="display: block; margin-bottom: 5px; font-weight: bold;">Working Days to Add:</label>
        <input type="number" id="daysToAdd" value="5" min="1" max="30" style="padding: 8px; border: 1px solid #ccc; border-radius: 4px; width: 100px;">
    </div>
    
<button onclick="calculateWorkingDay()" style="background: #0078d4; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold;">
        Calculate Working Day
    </button>
    
<div id="result" style="margin-top: 15px; padding: 10px; background: #e8f5e8; border-radius: 4px; display: none;">
        <strong>Result:</strong> <span id="resultDate"></span>
    </div>
</div>

## Email Domain Checker - Live Demo

<div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #28a745;">
    <h3>📧 Email Domain Validator</h3>
    <p>Test email domain validation:</p>
    
<div style="margin: 15px 0;">
        <label for="emailInput" style="display: block; margin-bottom: 5px; font-weight: bold;">Email Address:</label>
        <input type="email" id="emailInput" placeholder="user@example.com" style="padding: 8px; border: 1px solid #ccc; border-radius: 4px; width: 250px;">
    </div>
    
<button onclick="validateEmail()" style="background: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold;">
        Validate Domain
    </button>
    
<div id="emailResult" style="margin-top: 15px; padding: 10px; border-radius: 4px; display: none;">
        <strong>Validation Result:</strong> <span id="emailResultText"></span>
    </div>
</div>

<script>
function calculateWorkingDay() {
    const startDate = document.getElementById('startDate').value;
    const daysToAdd = parseInt(document.getElementById('daysToAdd').value);
    
    if (!startDate) {
        alert('Please select a start date');
        return;
    }
    
    // Simple working day calculation (excluding weekends)
    let currentDate = new Date(startDate);
    let addedDays = 0;
    
    while (addedDays < daysToAdd) {
        currentDate.setDate(currentDate.getDate() + 1);
        // Skip weekends (0 = Sunday, 6 = Saturday)
        if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
            addedDays++;
        }
    }
    
    const resultElement = document.getElementById('result');
    const resultDateElement = document.getElementById('resultDate');
    
    resultDateElement.textContent = currentDate.toLocaleDateString();
    resultElement.style.display = 'block';
}

function validateEmail() {
    const email = document.getElementById('emailInput').value;
    const resultElement = document.getElementById('emailResult');
    const resultTextElement = document.getElementById('emailResultText');
    
    if (!email) {
        alert('Please enter an email address');
        return;
    }
    
    // Simple email format validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValid = emailRegex.test(email);
    
    if (isValid) {
        resultElement.style.background = '#d4edda';
        resultElement.style.border = '1px solid #c3e6cb';
        resultTextElement.textContent = '✅ Valid email format detected';
    } else {
        resultElement.style.background = '#f8d7da';
        resultElement.style.border = '1px solid #f5c6cb';
        resultTextElement.textContent = '❌ Invalid email format';
    }
    
    resultElement.style.display = 'block';
}
</script>

## Ready to Implement?

{{< cards >}}
  {{< card link="/power-automate-connectors/calculate-working-day/" title="Get Calculate Working Day Connector" icon="calendar" tag="Free" tagColor="blue">}}
  {{< card link="/power-automate-connectors/email-domain-checker/" title="Get Email Domain Checker" icon="email-at" tag="Free" tagColor="green">}}
{{< /cards >}}
