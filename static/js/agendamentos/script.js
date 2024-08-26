


const tableBody = document.querySelector("tbody");

automacoes_json.forEach(item => {
    // Cria uma nova linha na tabela
    const row = document.createElement("tr");
    
    // Cria e preenche a célula para Entity ID
    const dispcell = document.createElement("td");
    dispcell.textContent = item.disp;
    row.appendChild(dispcell);
    
    // Cria e preenche a célula para State
    const stateCell = document.createElement("td");
    stateCell.textContent = item.entity_id;
    row.appendChild(stateCell);


    const teste = document.createElement("td");
    teste.textContent = item.state
    row.appendChild(teste);
    const on_off = document.createElement("td");
    on_off.innerHTML = '<input type="checkbox" id="'+item.id+'" value= "'+item.state+'"/><label for="'+item.id+'">Toggle</label>';
    row.appendChild(on_off);

    // Adiciona a linha completa à tabela
    tableBody.appendChild(row);

    check = document.getElementById(item.id)
    if (check.value == "on"){
        document.getElementById(item.id).checked = true;
    }



});








