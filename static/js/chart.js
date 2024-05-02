function getCryptoData(cryptoSymbol) {
  fetch(
    `https://api.coingecko.com/api/v3/coins/${cryptoSymbol}/market_chart?vs_currency=usd&days=1`
  )
    .then((response) => response.json())
    .then((data) => {
      var timestamps = data.prices.map((entry) => entry[0]);
      var prices = data.prices.map((entry) => entry[1]);

      var ctx = document.getElementById("cryptoChart").getContext("2d");

      // Détruire le graphique existant s'il y en a un
      if (window.cryptoChart instanceof Chart) {
        window.cryptoChart.destroy();
      }

      // Créer un nouveau graphique avec les nouvelles données
      window.cryptoChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: timestamps.map((timestamp) =>
            moment(timestamp).format("MMM DD, YYYY HH:mm")
          ),
          datasets: [
            {
              label: `Prix du ${cryptoSymbol.toUpperCase()} (USD)`,
              data: prices,
              backgroundColor: "rgba(54, 162, 235, 0.2)",
              borderColor: "rgba(54, 162, 235, 1)",
              borderWidth: 1,
              pointRadius: 0,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                type: "time",
                distribution: "linear",
                time: {
                  unit: "minute",
                },
                ticks: {
                  source: "auto",
                },
              },
            ],
            yAxes: [
              {
                ticks: {
                  beginAtZero: false,
                },
              },
            ],
          },
        },
      });
    })
    .catch((error) => {
      console.error(`Error fetching ${cryptoSymbol} data:`, error);
    });
}

document.getElementById("cryptoSelect").addEventListener("change", function () {
  var selectedCrypto = this.value;
  getCryptoData(selectedCrypto);
});

getCryptoData("bitcoin");
