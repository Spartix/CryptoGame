function getMatrix(matrixString) {
  var match = matrixString.match(
    /matrix\([^,]+,[^,]+,[^,]+,[^,]+,([^,]+),[^,]+\)/
  );

  // Si la correspondance est trouvée, extraire la valeur e
  if (match && match.length > 1) {
    var position4 = parseFloat(match[1]);
    return position4;
  } else {
    return 0;
  }
}

function IsDark() {
  var themeToggle = document.getElementById("theme-toggle");
  var transformValue =
    getComputedStyle(themeToggle).getPropertyValue("transform");
  if (getMatrix(transformValue) > 0) {
    return true;
  } else {
    return false;
  }
}
// var classiccolor = document.getElementsByClassName("welcome_message")[0].style;

// function inverseAllColors() {
//   var dico_class = {
//     "#161616": "white",
//     "#fff": "black",
//     black: "#fff",
//     white: "#161616",
//     transparent: "black",
//     "rgba(255, 255, 255, 0.7)": "rgba(0, 0, 0, 0.7)",
//     "rgba(0, 0, 0, 0.7)": "rgba(255, 255, 255, 0.7)",
//     // Ajoutez d'autres correspondances de couleurs au besoin
//   };

//   for (var i = 0; i < document.styleSheets.length; i++) {
//     var styleSheet = document.styleSheets[i];
//     try {
//       for (var j = 0; j < styleSheet.cssRules.length; j++) {
//         var rule = styleSheet.cssRules[j];

//         if (rule.type === 1) {
//           console.log(rule.style.color);
//           // Vérifier la couleur du texte
//           if (rule.style.color && dico_class[rule.style.color.toLowerCase()]) {
//             rule.style.color = dico_class[rule.style.color.toLowerCase()];
//           }
//           // Vérifier la couleur de fond
//           if (
//             rule.style.backgroundColor &&
//             dico_class[rule.style.backgroundColor.toLowerCase()]
//           ) {
//             rule.style.backgroundColor =
//               dico_class[rule.style.backgroundColor.toLowerCase()];
//           }
//           // Ajoutez d'autres propriétés CSS à inverser au besoin
//         }
//       }
//     } catch (error) {
//       console.error("Error accessing CSS rules:", error);
//     }
//   }
// }

function toggleTheme() {
  var themeToggle = document.getElementById("theme-toggle");
  themeToggle.classList.toggle("clicked");
  // inverseAllColors();
  console.log(IsDark());
  if (IsDark()) {
    console.log("dark mode on");
    document.body.style.backgroundColor = "#161616";
    var welcomeMessage = document.getElementsByClassName("welcome_message")[0];

    if (welcomeMessage) {
      welcomeMessage.style.fontSize = "7rem";
      welcomeMessage.style.color = "transparent";
      welcomeMessage.style.transform = "translate(5%, 40%)";
      welcomeMessage.style.fontFamily = "sans-serif";
      welcomeMessage.style.webkitTextStroke = "2px #fff";
      welcomeMessage.style.cursor = "pointer";
      welcomeMessage.style.transition = "all 0.4s ease";
      welcomeMessage.style.display = "inline-block";

      // Ajouter un écouteur d'événement pour gérer le survol
      welcomeMessage.addEventListener("mouseover", function () {
        this.style.color = "rgba(255, 255, 255, 0.7)";
        this.style.webkitTextStroke = "0";
      });

      // Ajouter un écouteur d'événement pour gérer la sortie du survol
      welcomeMessage.addEventListener("mouseout", function () {
        this.style.color = "transparent";
        this.style.webkitTextStroke = "2px #fff";
      });
    }

    var navLinks = document.querySelectorAll("nav ul li a");
    if (navLinks.length > 0) {
      navLinks.forEach((link) => {
        link.style.color = "azure";
      });
    }

    var labelElement = document.querySelector(".form-group label");

    if (labelElement) {
      labelElement.style.color = "azure"; // You can change 'red' to any color you want
    }
  } else {
    console.log("Light mode on");
    document.body.style.backgroundColor = "azure";
    var welcomeMessage = document.getElementsByClassName("welcome_message")[0];

    if (welcomeMessage) {
      welcomeMessage.style.color = "black";
    }

    var navLinks = document.querySelectorAll("nav ul li a");
    if (navLinks.length > 0) {
      navLinks.forEach((link) => {
        link.style.color = "#161616";
      });
    }
    var labelElement = document.querySelector(".form-group label");

    if (labelElement) {
      labelElement.style.color = "#161616"; // You can change 'red' to any color you want
    }
  }
}
