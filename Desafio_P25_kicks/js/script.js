let convidados = [];
        let ul = document.getElementById("lista");

        function cadastra_convidado() {
            let convidado = document.getElementById("i_convidado").value;
            if (convidado !== "") {
                convidados.push(convidado);
                document.getElementById("i_convidado").value = "";
                desenha_lista();
            }
        }

        function remove_convidado(index) {
            convidados.splice(index, 1);
            desenha_lista();
        }

        function desenha_lista() {
            ul.innerHTML = "";
            for (let x = 0; x < convidados.length; x++) {
                ul.innerHTML += `
                    <li>
                        ${convidados[x]}
                        <button class="delete-btn" onclick="remove_convidado(${x})">Remover</button>
                    </li>`;
            }
        }
        