window.onload = function () {
    var barra = document
    .getElementById("sidenav_ul")
    .addEventListener("mouseover", function () {
      var sidenav = document.getElementById("sidenav");
      var main = document.getElementById("main");
      var sensor = document.getElementById("sensores");
      var btn1 = document.getElementById("config1");
      var btn2 = document.getElementById("config2");
      var btn3 = document.getElementById("config3");
      btn3.style.left = "60em";
      btn2.style.left = "60em";
      btn1.style.left = "60em";
      sidenav.style.width = "230px";
      main.style.marginLeft = "270px";
      sensor.style.width = "85.5rem";
    });
  var barra = document
    .getElementById("sidenav_ul")
    .addEventListener("mouseout", function () {
      var sidenav = document.getElementById("sidenav");
      var main = document.getElementById("main");
      var sensor = document.getElementById("sensores");
      var btn1 = document.getElementById("config1");
      var btn2 = document.getElementById("config2");
      var btn3 = document.getElementById("config3");
      sidenav.style.width = "65px";
      main.style.marginLeft = "120px";
      sensor.style.width = "98rem";
      btn3.style.left = "60em";
      btn2.style.left = "60em";
      btn1.style.left = "60em";
    });
  function tela_sensor(tela, botao, icon) {
    var on_off = 0;
    var click = document
      .getElementById(botao)
      .addEventListener("click", function () {
        var botao = document.getElementById(icon);
        var obj = document.getElementById(tela);

        if (on_off == 0) {
          obj.style.height = "40rem";
          botao.style.top = "47em";

          on_off = 1;
        } else {
          obj.style.height = "200px";
          botao.style.top = "13em";
          on_off = 0;
        }
      });
  }
  tela_sensor("sensor1", "config1", "config1");
  tela_sensor("sensor2", "config2", "config2");
  tela_sensor("sensor3", "config3", "config3");
}