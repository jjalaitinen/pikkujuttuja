function kirjoitaSivulle(elementti) {
  document.getElementById("tulostus").textContent += elementti.outerHTML;
}

function tyhjennaLomake() {
  let albuminNimiInput = document.getElementById("albumin_nimi");
  albuminNimiInput.value = "";

  let artistiInput = document.getElementById("artisti");
  artistiInput.value = "";

  let kansikuvaInput = document.getElementById("kansikuva");
  kansikuvaInput.value = "";
}

function teeLevy(e) {
  e.preventDefault();

  let albuminNimi = document.getElementById("albumin_nimi").value;
  let artisti = document.getElementById("artisti").value;
  let kansikuva = document.getElementById("kansikuva").value;

  let uusi_li = document.createElement("li");
  uusi_li.setAttribute("id", artisti + "-" + albuminNimi);

  let uusi_img = document.createElement("img");
  uusi_img.setAttribute("src", kansikuva);
  uusi_img.setAttribute("alt", artisti + "_" + albuminNimi);

  uusi_li.appendChild(uusi_img);

  kirjoitaSivulle(uusi_li);
  tyhjennaLomake();
}

window.addEventListener("load", function () {
  let painike = document.getElementsByTagName("button")[0];
  painike.addEventListener("click", teeLevy);
});
