

window.onload = function (){
        
  var barra = document.getElementById('sidenav_ul').addEventListener("mouseover",function(){
    var sidenav = document.getElementById('sidenav');
    var main = document.getElementById('main');
    sidenav.style.width = "230px";
    main.style.marginLeft ="270px"
  })
  var barra = document.getElementById('sidenav_ul').addEventListener("mouseout",function(){ 
    var sidenav = document.getElementById('sidenav');
    var main = document.getElementById('main');
    sidenav.style.width = "65px";
    main.style.marginLeft = "120px"
  })
  

}