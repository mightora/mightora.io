# Analytics

<canvas id="lineChart" width="400" height="200"></canvas>

<div id="hitsCard" style="margin-top: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 200px;">
    <h3>Hits in the Last Week</h3>
    <p id="hitsCount">Loading...</p>
</div>

<script>
console.log("Script loaded");

async function fetchData() {
    console.log("Fetching data...");
    const response = await fetch('https://stmightoriaprod01.blob.core.windows.net/analytics/api-mightoria.json');
    const jsonData = await response.json();
    console.log("Data fetched:", jsonData);

    // Extract and group the relevant data by month
    const data = jsonData.data.viewer.zones[0].httpRequests1dGroups.reduce((acc, group) => {
        const date = new Date(group.dimensions.date);
        const month = date.getFullYear() + '-' + (date.getMonth() + 1).toString().padStart(2, '0');
        if (!acc[month]) {
            acc[month] = 0;
        }
        acc[month] += group.sum.requests;
        return acc;
    }, {});

    // Convert the grouped data into an array of objects
    const processedData = Object.keys(data).map(month => ({
        date: month,
        value: data[month]
    }));

    console.log("Processed data:", processedData);
    return processedData;
}

function renderChart(data) {
    console.log("Rendering chart...");
    const ctx = document.getElementById('lineChart').getContext('2d');
    const labels = data.map(item => item.date);
    const values = data.map(item => item.value);

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Requests',
                data: values,
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
                        text: 'Month'
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

function calculateHitsLastWeek(data) {
    const oneWeekAgo = new Date();
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);

    const hitsLastWeek = data.reduce((total, item) => {
        const date = new Date(item.date);
        if (date >= oneWeekAgo) {
            total += item.value;
        }
        return total;
    }, 0);

    return hitsLastWeek;
}

fetchData().then(data => {
    renderChart(data);
    const hitsLastWeek = calculateHitsLastWeek(data);
    document.getElementById('hitsCount').innerText = hitsLastWeek.toLocaleString();
}).catch(error => console.error("Error fetching data:", error));
</script>