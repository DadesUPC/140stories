function tweetProgressBar() {
  var bar = document.getElementById("progress-bar-fill");
  var textarea = document.getElementById("tweet-box");
  var width = 0;
  var hue = 0;
  var len = textarea.value.length;
  width = Math.round(len / 1.4);
  bar.style.width = width + '%';
  
  /* GRADIENT HUE */
  /*
  hue = 78 - 0.0078 * Math.pow(width, 2);
  bar.style.backgroundColor = "hsl(" + hue + ",38.4%,47.2%)";
  */

  /* NO HUE */
  /*
  if (width == 100)
  {
    bar.style.backgroundColor = "#AF4B4B";
  }
  else
  {
    bar.style.backgroundColor = "#4CAF50";
  }
  */
}

document.getElementById("tweet-box").oninput = function () {tweetProgressBar()};