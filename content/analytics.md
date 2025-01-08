# Transparent Insights Into Our Tools

At Mightora.io, we are passionate about empowering the **Power Platform community** with tools that integrate seamlessly with Azure, Power Platform, and Azure DevOps. Ensuring these tools deliver real value is a top priority for us.

To achieve this, we track tool usage to understand how our community interacts with the resources we provide. Below, we’ve shared some key stats to give you a transparent view of how our tools are being used.


## Your Privacy Matters

We value your privacy. Usage tracking is limited to recording a hit on our Cloudflare hosted endpoint whenever a tool is accessed. No personal data or additional information is collected—just the essentials to help us improve.


## Analytics

<div style="display: flex; flex-wrap: wrap; gap: 20px;">
    <div id="hitsCard" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 200px;">
        <h3>Hits in the Last Week</h3>
        <p id="hitsCount">Loading...</p>
    </div>

 <div id="monthlyHitsCard" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 200px;">
        <h3>Hits in the Last Month</h3>
        <p id="monthlyHitsCount">Loading...</p>
    </div>

  <div id="yearlyHitsCard" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 200px;">
        <h3>Hits in the Last Year</h3>
        <p id="yearlyHitsCount">Loading...</p>
    </div>
</div>

<canvas id="lineChart" width="400" height="200" style="margin-top: 20px;"></canvas>

<script>
console.log("Script loaded");

async function fetchData() {
    console.log("Fetching data...");
    const response = await fetch('https://stmightoriaprod01.blob.core.windows.net/analytics/api-mightoria.json');
    const jsonData = await response.json();
    console.log("Data fetched:", jsonData);

    // Extract the relevant data by day
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
        console.log("Processing date:", date, "One week ago:", oneWeekAgo);
        if (date >= oneWeekAgo) {
            total += item.requests;
        }
        return total;
    }, 0);

    console.log("Hits last week:", hitsLastWeek);
    return hitsLastWeek;
}

function calculateHitsLastMonth(data) {
    const oneMonthAgo = new Date();
    oneMonthAgo.setMonth(oneMonthAgo.getMonth() - 1);
    console.log("One month ago:", oneMonthAgo);

    const hitsLastMonth = data.reduce((total, item) => {
        const date = new Date(item.date);
        console.log("Processing date:", date, "One month ago:", oneMonthAgo);
        if (date >= oneMonthAgo) {
            total += item.requests;
        }
        return total;
    }, 0);

    console.log("Hits last month:", hitsLastMonth);
    return hitsLastMonth;
}

function calculateHitsLastYear(data) {
    const oneYearAgo = new Date();
    oneYearAgo.setFullYear(oneYearAgo.getFullYear() - 1);
    console.log("One year ago:", oneYearAgo);

    const hitsLastYear = data.reduce((total, item) => {
        const date = new Date(item.date);
        if (date >= oneYearAgo) {
            total += item.requests;
        }
        return total;
    }, 0);

    console.log("Hits last year:", hitsLastYear);
    return hitsLastYear;
}

function renderChart(data) {
    console.log("Rendering chart...");

    // Group the data by month for the chart
    const groupedData = data.reduce((acc, item) => {
        const date = new Date(item.date);
        const month = date.getFullYear() + '-' + (date.getMonth() + 1).toString().padStart(2, '0');
        if (!acc[month]) {
            acc[month] = 0;
        }
        acc[month] += item.requests;
        return acc;
    }, {});

    // Convert the grouped data into an array of objects
    const chartData = Object.keys(groupedData).map(month => ({
        date: month,
        value: groupedData[month]
    }));

    const ctx = document.getElementById('lineChart').getContext('2d');
    const labels = chartData.map(item => item.date);
    const values = chartData.map(item => item.value);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Requests',
                data: values,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'month'
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Requests'
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom'
                }
            }
        }
    });
    console.log("Chart rendered");
}

fetchData().then(data => {
    const hitsLastWeek = calculateHitsLastWeek(data);
    document.getElementById('hitsCount').innerText = hitsLastWeek.toLocaleString();

    const hitsLastMonth = calculateHitsLastMonth(data);
    document.getElementById('monthlyHitsCount').innerText = hitsLastMonth.toLocaleString();

    const hitsLastYear = calculateHitsLastYear(data);
    document.getElementById('yearlyHitsCount').innerText = hitsLastYear.toLocaleString();

    renderChart(data);
}).catch(error => console.error("Error fetching data:", error));
</script>