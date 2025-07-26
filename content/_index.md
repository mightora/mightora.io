---
title: unleash the might of automation
toc: false
---

</br>

<a href="/analytics" style="text-decoration: none; color: inherit;">
    <div id="hitsCard" style="margin-top: 5px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 100%; height: 40px; display: flex; align-items: center; justify-content: center;">
        <div id="hitsCount" style="font-size: 24px; font-weight: bold; margin-right: 10px;">Loading...</div>
        <div style="margin: 0;">hits on our tools in the Last Week, view our stats here</div>
    </div>
</a>

<script>
console.log("Script loaded");

async function fetchData() {
    console.log("Fetching data...");
    const response = await fetch('https://stmightoriaprod01.blob.core.windows.net/analytics/api-mightoria.json');
    const jsonData = await response.json();
    console.log("Data fetched:", jsonData);

    // Extract and group the relevant data by day
    const data = jsonData.data.viewer.zones[0].httpRequests1dGroups.map(group => ({
        date: group.dimensions.date,
        requests: group.sum.requests
    }));

    console.log("Processed data:", data);
    return data;
}

function calculateHitsLastWeek(data) {
    const oneWeekAgo = new Date();
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
    console.log("One week ago:", oneWeekAgo);

    const hitsLastWeek = data.reduce((total, item) => {
        const date = new Date(item.date);
        if (date >= oneWeekAgo) {
            total += item.requests;
        }
        return total;
    }, 0);

    console.log("Hits last week:", hitsLastWeek);
    return hitsLastWeek;
}

function calculateHitsYesterday(data) {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toISOString().split('T')[0];
    console.log("Yesterday:", yesterdayStr);

    const hitsYesterday = data.reduce((total, item) => {
        if (item.date === yesterdayStr) {
            total += item.requests;
        }
        return total;
    }, 0);

    console.log("Hits yesterday:", hitsYesterday);
    return hitsYesterday;
}

document.addEventListener('DOMContentLoaded', () => {
    fetchData().then(data => {
        const hitsLastWeek = calculateHitsLastWeek(data);
        document.getElementById('hitsCount').innerText = hitsLastWeek.toLocaleString();

        const hitsYesterday = calculateHitsYesterday(data);
        document.getElementById('yesterdayHitsCount').innerText = hitsYesterday.toLocaleString();
    }).catch(error => console.error("Error fetching data:", error));
});
</script>

</a>

</br>

<div id="slider" style="width: 100%; overflow: hidden; position: relative; border: 2px solid #0078d4; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    <div id="sliderContent" style="display: flex; transition: transform 0.5s ease-in-out;">
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: #f9f9f9; display: flex; align-items: center; justify-content: center;">
                <img src="https://raw.githubusercontent.com/TechTweedie/techtweedie.github.io/main/static/logo-01_150x150.png" alt="Tech Tweedie Logo" style="width: 100px; height: 100px;">
            </div>
            <div style="flex: 70%; padding: 20px; text-align: center; display: flex; flex-direction: column; justify-content: center; background-color: #f9f9f9;">
                <p style="font-size: 18px; font-weight: bold; color: #333;">Discover a suite of automations designed to streamline your development on the Power Platform. For more information, feel free to reach out via the contact button below.</p>
            </div>
        </div>
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: #f1f1f1; display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 50px; height: 50px; color: #0078d4;"><path stroke-linecap="round" stroke-linejoin="round" d="M15.59 14.37a6 6 0 0 1-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 0 0 6.16-12.12A14.98 14.98 0 0 0 9.631 8.41m5.96 5.96a14.926 14.926 0 0 1-5.841 2.58m-.119-8.54a6 6 0 0 0-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 0 0-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 0 1-2.448-2.448 14.9 14.9 0 0 1 .06-.312m-2.24 2.39a4.493 4.493 0 0 0-1.757 4.306 4.493 4.493 0 0 0 4.306-1.758M16.5 9a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z" /></svg>
            </div>
            <div style="flex: 70%; padding: 20px; text-align: left; background-color: #f1f1f1;">
                <h3 style="font-size: 22px; color: #0078d4;">CI/CD Tools</h3>
                <p style="font-size: 16px; color: #555;">Boost your CI/CD pipelines with our powerful Azure DevOps Extensions. Designed for seamless integration.</p>
                <a href="/pipeline-tools/" style="text-decoration: none; color: #0078d4; font-weight: bold; font-size: 16px;">Discover Extensions</a>
            </div>
        </div>
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: white; display: flex; align-items: center; justify-content: center;">
                <img src="https://raw.githubusercontent.com/TechTweedie/techtweedie.github.io/main/static/logo-01_150x150.png" alt="Tech Tweedie Logo" style="width: 100px; height: 100px;">
            </div>
            <div style="flex: 70%; padding: 20px; text-align: left; background-color: white;">
                <h3 style="font-size: 22px; color: #0078d4;">Free Tools by Tech Tweedie</h3>
                <p style="font-size: 16px; color: #555;">All these tools are proudly brought to you by Tech Tweedie. Empowering developers worldwide.</p>
            </div>
        </div>
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: #e8f5e9; display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" viewBox="0 0 16 16" style="color: #4caf50;"><path d="M8 0a8 8 0 1 0 8 8A8 8 0 0 0 8 0zm3.93 6.588l-4 5a.5.5 0 0 1-.76.063L4.07 8.588a.5.5 0 1 1 .76-.65L7.5 10.293l3.67-4.585a.5.5 0 0 1 .76.65z"/></svg>
            </div>
            <div style="flex: 70%; padding: 20px; text-align: left; background-color: #e8f5e9;">
                <h3 style="font-size: 22px; color: #4caf50;">Email Domain Checker</h3>
                <p style="font-size: 16px; color: #555;">Validate email domains effortlessly with our Email Domain Checker. Perfect for ensuring data accuracy.</p>
                <a href="/power-automate-connectors/email-domain-checker/" style="text-decoration: none; color: #4caf50; font-weight: bold; font-size: 16px;">Try Now</a>
            </div>
        </div>
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: #e3f2fd; display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" viewBox="0 0 16 16" style="color: #2196f3;"><path d="M8 0a8 8 0 1 0 8 8A8 8 0 0 0 8 0zm3.93 6.588l-4 5a.5.5 0 0 1-.76.063L4.07 8.588a.5.5 0 1 1 .76-.65L7.5 10.293l3.67-4.585a.5.5 0 0 1 .76.65z"/></svg>
            </div>
            <div style="flex: 70%; padding: 20px; text-align: left; background-color: #e3f2fd;">
                <h3 style="font-size: 22px; color: #2196f3;">Calculate Working Day</h3>
                <p style="font-size: 16px; color: #555;">Easily calculate working days between dates with our specialized tool. Ideal for project planning.</p>
                <a href="/power-automate-connectors/calculate-working-day/" style="text-decoration: none; color: #2196f3; font-weight: bold; font-size: 16px;">Learn More</a>
            </div>
        </div>
        <div style="min-width: 100%; display: flex;">
            <div style="flex: 30%; background-color: #fff3e0; display: flex; align-items: center; justify-content: center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" viewBox="0 0 16 16" style="color: #ff9800;"><path d="M8 0a8 8 0 1 0 8 8A8 8 0 0 0 8 0zm3.93 6.588l-4 5a.5.5 0 0 1-.76.063L4.07 8.588a.5.5 0 1 1 .76-.65L7.5 10.293l3.67-4.585a.5.5 0 0 1 .76.65z"/></svg>
            </div>
            <div style="flex: 70%; padding: 20px; text-align: left; background-color: #fff3e0;">
                <h3 style="font-size: 22px; color: #ff9800;">Dataverse 4 Teams Tools</h3>
                <p style="font-size: 16px; color: #555;">Enhance your Dataverse for Teams experience with our powerful tools. Simplify your workflows today.</p>
                <a href="/pipeline-tools/dataverse-4-teams-tools/" style="text-decoration: none; color: #ff9800; font-weight: bold; font-size: 16px;">Explore Tools</a>
            </div>
        </div>
    </div>
    <button id="prev" style="position: absolute; top: 50%; left: 10px; transform: translateY(-50%); background-color: #0078d4; color: white; border: none; border-radius: 50%; width: 30px; height: 30px; font-size: 14px; cursor: pointer; opacity: 0.7;">&#10094;</button>
    <button id="next" style="position: absolute; top: 50%; right: 10px; transform: translateY(-50%); background-color: #0078d4; color: white; border: none; border-radius: 50%; width: 30px; height: 30px; font-size: 14px; cursor: pointer; opacity: 0.7;">&#10095;</button>
</div>

<script>
    const sliderContent = document.getElementById('sliderContent');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');

    let currentIndex = 0;
    const totalSlides = 5; // Update this if you add more slides
    const autoSlideInterval = 5000; // 5 seconds

    function updateSlider() {
        sliderContent.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalSlides - 1;
        updateSlider();
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex < totalSlides - 1) ? currentIndex + 1 : 0;
        updateSlider();
    });

    // Auto-slide functionality
    setInterval(() => {
        currentIndex = (currentIndex < totalSlides - 1) ? currentIndex + 1 : 0;
        updateSlider();
    }, autoSlideInterval);
</script>

</br>

## Explore

{{< cards >}}
  {{< card link="/tools/power-automate-templates/auto-tag-devops-tickets-into-emails/" title="Auto Tag DevOp sTickets into Emails" icon="email-at" tag="Email" tagColor="blue">}}
  {{< card link="/power-automate-connectors/calculate-working-day/" title="Calculate Working Day" icon="calendar" tag="Calendar" tagColor="blue">}}
  {{< card link="/pipeline-tools/dataverse-4-teams-tools/" title="Dataverse 4 Teams Tools" icon="powershell" tag="Powershell" tagColor="green">}}
  {{< card link="/power-automate-connectors/email-domain-checker/" title="Email Domain Checker" icon="email-at" tag="Email" tagColor="blue">}}
  {{< card link="/pipeline-tools/" title="Pipeline Tools" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/pipeline-tools/playwright-for-power-platform/" title="Playwright for Power Platform DevOps Extension" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/power-automate-connectors/" title="Power Automate Connectors" icon="powerautomate" tag="Flow" tagColor="blue">}}
  {{< card link="/tools/power-automate-templates/" title="Power Automate Templates" icon="powerautomate" tag="Flow" tagColor="blue">}}
  {{< card link="/pipeline-tools/power-platform-devops-extension/" title="Power Platform DevOps Extension" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/power-automate-connectors/send-email-with-graph/" title="Send Email with Graph" icon="email-at" tag="Email" tagColor="blue">}}
{{< /cards >}}
 
## About

Mightora.io is dedicated to helping other developers with the Power Platform. Through mightora.io, we share our Power Automate Connectors and Functions, along with Azure DevOps (ADO) extensions designed to make it easier to work with the Power Platform inside Pipelines on ADO. 
Our goal is to not only reduce your development costs but also empower your developers to embrace citizen development.
Mightora’s tools are all from TechTweedie. For more information, visit [techtweedie.github.io](https://techtweedie.github.io) or [iantweedie.biz](https://iantweedie.biz).


{{< cards >}}
  {{< card link="/tools/power-automate-templates/auto-tag-devops-tickets-into-emails/" title="Auto Tag DevOp sTickets into Emails" icon="email-at" tag="Email" tagColor="blue">}}
  {{< card link="/power-automate-connectors/calculate-working-day/" title="Calculate Working Day" icon="calendar" tag="Calendar" tagColor="blue">}}
  {{< card link="/pipeline-tools/dataverse-4-teams-tools/" title="Dataverse 4 Teams Tools" icon="powershell" tag="Powershell" tagColor="green">}}
  {{< card link="/power-automate-connectors/email-domain-checker/" title="Email Domain Checker" icon="email-at" tag="Email" tagColor="blue">}}
  {{< card link="/pipeline-tools/" title="Pipeline Tools" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/pipeline-tools/playwright-for-power-platform/" title="Playwright for Power Platform DevOps Extension" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/power-automate-connectors/" title="Power Automate Connectors" icon="powerautomate" tag="Flow" tagColor="blue">}}
  {{< card link="/tools/power-automate-templates/" title="Power Automate Templates" icon="powerautomate" tag="Flow" tagColor="blue">}}
  {{< card link="/pipeline-tools/power-platform-devops-extension/" title="Power Platform DevOps Extension" icon="rocket" tag="Pipeline" tagColor="green">}}
  {{< card link="/power-automate-connectors/send-email-with-graph/" title="Send Email with Graph" icon="email-at" tag="Email" tagColor="blue">}}
{{< /cards >}}

</br>
