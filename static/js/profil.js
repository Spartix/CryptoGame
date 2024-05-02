function Me() {
  var xhr = new XMLHttpRequest();

  xhr.open("GET", "/@Me", true);

  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      var response = JSON.parse(xhr.responseText);

      document.getElementById("Pseudo").value = response["Username"];
      document.getElementById("email").value = response["email"];
    } else {
      console.error("La requête a échoué avec le statut: " + xhr.status);
    }
  };

  xhr.onerror = function () {
    console.error("Une erreur réseau s'est produite");
  };

  xhr.send();
}
Me();

function fetchActifs() {
  var xhr = new XMLHttpRequest();

  xhr.open("GET", "/Balance", true);

  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      var response = JSON.parse(xhr.responseText);

      var selectElement = document.getElementById("actifSelect");

      selectElement.addEventListener("change", function () {
        var balanceElement = document.querySelector(
          "input[placeholder='BALANCE']"
        );

        var selectedActif = selectElement.value;

        if (response[selectedActif] !== undefined) {
          balanceElement.value = response[selectedActif];
        } else {
          balanceElement.value = "";
        }
      });
    } else {
      console.error("La requête a échoué avec le statut: " + xhr.status);
    }
  };

  xhr.onerror = function () {
    console.error("Une erreur réseau s'est produite");
  };

  xhr.send();
}

fetchActifs();

function parseJwt(token) {
  var base64Url = token.split(".")[1];
  var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  var jsonPayload = decodeURIComponent(
    atob(base64)
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );
  return JSON.parse(jsonPayload);
}

console.log(
  parseJwt((Token = document.cookie.split("access_token=")[1].split("&")[0]))
);
