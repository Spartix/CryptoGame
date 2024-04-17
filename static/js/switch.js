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
function toggleTheme() {
  var themeToggle = document.getElementById("theme-toggle");
  themeToggle.classList.toggle("clicked");
  console.log(IsDark());
  if (IsDark()) {
    console.log("dark mode on");
    document.body.style.backgroundColor = "#161616";
  } else {
    console.log("Light mode on");
    document.body.style.backgroundColor = "#3f3f3f";
  }
}
