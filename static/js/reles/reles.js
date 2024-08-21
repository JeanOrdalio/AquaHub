


window.onload = function () {

///Anim reles

  function evento(rele, botao, icon) {
    var on_off = 0;
    var click = document
      .getElementById(botao)
      .addEventListener("click", function () {
        var botao = document.getElementById(icon);
        var obj = document.getElementById(rele);

        if (on_off == 0) {
          obj.style.height = "400px";
          botao.style.top = "335px";
          console.log(botao.style)

          on_off = 1;
        } else {
          obj.style.height = "100px";
          botao.style.top = "32px";
          on_off = 0;
        }
      });
  }
  evento("rele1", "config1", "config1");
  evento("rele2", "config2", "config2");
  evento("rele3", "config3", "config3");
  evento("rele4", "config4", "config4");
  evento("rele5", "config5", "config5");
  evento("rele6", "config6", "config6");
  evento("rele7", "config7", "config7");
  evento("rele8", "config8", "config8");


///Anim SideNav

var barra = document.getElementById('sidenav_ul').addEventListener("mouseover", function () {
var sidenav = document.getElementById('sidenav');
var main = document.getElementById('main');
sidenav.style.width = "230px";
main.style.marginLeft = "270px"
})
var barra = document.getElementById('sidenav_ul').addEventListener("mouseout", function () {
var sidenav = document.getElementById('sidenav');
var main = document.getElementById('main');
sidenav.style.width = "65px";
main.style.marginLeft = "120px";
})

};



