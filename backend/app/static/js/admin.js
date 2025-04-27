// Admin Dashboard: Display chart (mock example)
document.addEventListener('DOMContentLoaded', function () {
    const chartData = [30, 45, 20, 55, 80];
    const chart = document.getElementById('adminChart');
    chart.height = 150;
    const ctx = chart.getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Mess Usage',
                data: chartData,
                borderColor: 'rgb(0, 255, 255)',
                tension: 0.1
            }]
        }
    });
});
