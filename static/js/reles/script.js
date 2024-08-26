function validade(data_form,checkbox) {
  const checkboxes = document.querySelectorAll("input[type=checkbox]:checked");
  var form = document.getElementById(data_form);
  var input = document.getElementById(checkbox);
  for (let checkbox of checkboxes) {
    var check = checkbox.dataset.id;
    input.value = check;
    form.submit();
    alert("teste");
  }
}

function btn_tela1(auto1,auto2) {
  var tela1 = document.getElementById(auto1);
  var tela2 = document.getElementById(auto2);
  if (tela1.style.display == "none") {
    tela1.style.display = "flex";
    tela2.style.display = "none";
  }
  if (tela2.style.display = "flex")
    tela2.style.display = "none"
    tela1.style.display = "flex";

}

function btn_tela2(auto1,auto2) {
    var tela2 = document.getElementById(auto1);
    var tela1 = document.getElementById(auto2);
    if (tela2.style.display = "none"){
      tela2.style.display = "flex";
      tela1.style.display = "none";
    }
    if (tela1.style.display = "flex"){
        tela1.style.display = "none"
        tela2.style.display = "flex"
    }}

