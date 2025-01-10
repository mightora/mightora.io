---
title: unleash the might of automation with free tools from TechTweedie
toc: false
---

We have built a number of automations to assist your development on the Power Platform. For more infoamtion please free to reachout to me via the contact button. 

</br>

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

## Explore

{{< cards >}}
  {{< card link="/power-automate-connectors/calculate-working-day/" title="Calculate Working Day" icon="calendar" tag="Flow"  tagColor="blue">}}
  {{< card link="/power-automate-connectors/email-domain-checker/" title="Email Domain Checker" icon="email-at" tag="Flow" tagColor="blue">}}
  {{< card link="/pipeline-tools/dataverse-4-teams-tools/" title="Dataverse 4 Teams Tools" icon="powershell" tag="Powershell"  tagColor="green">}}
{{< /cards >}}
 
## About

Mightora.io is dedicated to helping other developers with the Power Platform. Through mightora.io, we share our Power Automate Connectors and Functions, along with Azure DevOps (ADO) extensions designed to make it easier to work with the Power Platform inside Pipelines on ADO. 
Our goal is to not only reduce your development costs but also empower your developers to embrace citizen development.
Mightora’s tools are all from TechTweedie. For more information, visit [techtweedie.github.io](https://techtweedie.github.io) or [iantweedie.biz](https://iantweedie.biz).


{{< cards >}}
  {{< card link="/about/" title="Find out more about mightora.io">}}
{{< /cards >}}

