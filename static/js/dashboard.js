window.onload = function () {
  /* Grafico 1 */
  
  const labels_hum = sensorhum_json.map((item) => item.Hora);
  const estado_hum = sensorhum_json.map((item) => item.Estado);
  const valormin_hum = Math.min(...estado_hum);
  const valormax_hum = Math.max(...estado_hum);
  const Sensorhum = document.getElementById("Sensorhum");

  new Chart(Sensorhum, {
    type: "line",
    data: {
      labels: labels_hum,
      datasets: [
        {
          label: "Humidade",
          data: estado_hum,
          borderWidth: 3,
          fill: true,
          tension: 0.5,
          backgroundColor: "rgb(255, 99, 71)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          min: valormin_hum,
          max: valormax_hum,
        },
      },
    },
  });

  /* Grafico 2 */

  const labels_2 = sensor2_json.map((item) => item.Hora);
  const estado_2 = sensor2_json.map((item) => item.Estado);
  const valormin_2 = Math.min(...estado_2);
  const valormax_2 = Math.max(...estado_2);
  const Sensor2 = document.getElementById("Sensor2");

  new Chart(Sensor2, {
    type: "line",
    data: {
      labels: labels_2,
      datasets: [
        {
          label: "Temperatura",
          data: estado_2,
          borderWidth: 3,
          fill: true,
          tension: 0.5,
          backgroundColor: "rgb(255, 165, 0)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          min: valormin_2,
          max: valormax_2,
        },
      },
    },
  });

  /* Grafico 3 */

  const labels_1 = sensor1_json.map((item) => item.Hora);
  const estado_1 = sensor1_json.map((item) => item.Estado);
  const valormin_1 = Math.min(...estado_1);
  const valormax_1 = Math.max(...estado_1);
  const Sensor1 = document.getElementById("Sensor1");

  new Chart(Sensor1, {
    type: "line",
    data: {
      labels: labels_1,
      datasets: [
        {
          label: "Temperatura",
          data: estado_1,
          borderWidth: 3,
          fill: true,
          tension: 0.5,
          backgroundColor: "rgb(60, 179, 113)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          min: valormin_1,
          max: valormax_1,
        },
      },
    },
  });
  var barra = document
    .getElementById("sidenav_ul")
    .addEventListener("mouseover", function () {
      var sidenav = document.getElementById("sidenav");
      var main = document.getElementById("main");
      var reles_container = document.getElementById("reles_container");
      sidenav.style.width = "230px";
      main.style.marginLeft = "245px";
      main.style.columnGap = "0px";
      reles_container.style.columnGap = "15px";
    });
  var barra = document
    .getElementById("sidenav_ul")
    .addEventListener("mouseout", function () {
      var sidenav = document.getElementById("sidenav");
      var main = document.getElementById("main");
      var reles_container = document.getElementById("reles_container");
      sidenav.style.width = "65px";
      main.style.marginLeft = "88px";
      main.style.columnGap = "45px";
      reles_container.style.columnGap = "58px";
    });

function status(rele,estadodb){
var  alvo = document.getElementById(rele);
var estado = estadodb
if (estado == 1){
  alvo.style.animationName ="status_rele"
  alvo.style.backgroundImage = "radial-gradient( #00ff15de,#da575700)";
 
}
if (estado == 0){
  alvo.style.animationName ="status_rele"
  alvo.style.backgroundImage = "radial-gradient( #ff0000e5,#da575700)";
}
} 

status("rele1",rele1),status("rele2",rele2),status("rele3",rele3),status("rele4",rele4),status("rele5",rele3),status("rele6",rele4)
status("rele7",rele1),status("rele8",rele2)
}

