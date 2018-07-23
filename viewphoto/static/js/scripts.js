function copyLink() {
  var copyText = document.getElementById("link");
  copyText.select();
  document.execCommand("Copy");
  alert("Copied the text: " + copyText.value);
}
