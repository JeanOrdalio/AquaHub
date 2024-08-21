function validade() {
  const checkboxes = document.querySelectorAll("input[type=checkbox]:checked");
  var form = document.getElementById("data_auto");
  var input = document.getElementById("checkbox1");
  for (let checkbox of checkboxes) {
    var check = checkbox.dataset.id;
    input.value = check;
    form.submit();
    alert("teste");
  }
}

function btn_tela1() {
  var tela1 = document.getElementById("data");
  var tela2 = document.getElementById("disp");
  if (tela1.style.display == "none") {
    tela1.style.display = "flex";
    tela2.style.display = "none";
  }
  if (tela2.style.display = "flex")
    tela2.style.display = "none"
    tela1.style.display = "flex";

}

function btn_tela2() {
    var tela2 = document.getElementById("disp");
    var tela1 = document.getElementById("data");
    if (tela2.style.display = "none"){
      tela2.style.display = "flex";
      tela1.style.display = "none";
    }
    if (tela1.style.display = "flex"){
        tela1.style.display = "none"
        tela2.style.display = "flex"
    }}
