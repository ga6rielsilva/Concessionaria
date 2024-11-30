document.addEventListener("DOMContentLoaded", function () {

    // Traduzindo placeholder {Ydate}
    const YdatePlaceholder = document.getElementById("Ydate");
    if (YdatePlaceholder) {
        const date = new Date();
        YdatePlaceholder.innerHTML = "&nbsp;" + date.getFullYear() + "&nbsp;";
    }

    // Código do submenu do usuário
    const userIcon = document.getElementById("user-icon");
    const userSubmenu = document.getElementById("user-submenu");

    if (userIcon && userSubmenu) {

        userIcon.addEventListener("click", function (event) {
            event.preventDefault();

            if (userSubmenu.style.display === "block") {
                userSubmenu.style.display = "none";
            } else {
                userSubmenu.style.display = "block";
            }
        });

        window.addEventListener("click", function (event) {
            if (!userIcon.contains(event.target) && !userSubmenu.contains(event.target)) {
                userSubmenu.style.display = "none";
            }
        });
    }

    // Validação do CPF e máscara
    const cpfok = document.getElementById("cpf");

    if (cpfok) {

        function validarCPF(cpf) {
            const cpfNumeros = cpf.replace(/\D/g, "");
            if (cpfNumeros.length !== 11) return false;

            const cpfArray = Array.from(cpfNumeros);
            let soma = 0;

            for (let i = 0; i < 9; i++) {
                soma += parseInt(cpfArray[i]) * (10 - i);
            }

            let resto = (soma * 10) % 11;
            let digitoVerificador = resto === 10 ? 0 : resto;

            if (digitoVerificador !== parseInt(cpfArray[9])) return false;

            soma = 0;

            for (let i = 0; i < 10; i++) {
                soma += parseInt(cpfArray[i]) * (11 - i);
            }

            resto = (soma * 10) % 11;
            digitoVerificador = resto === 10 ? 0 : resto;

            return digitoVerificador === parseInt(cpfArray[10]);
        }

        function aplicarMascara(cpf) {
            return cpf.replace(/\D/g, "")
                .replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
        }

        cpfok.addEventListener("input", function (event) {
            let cpf = event.target.value;

            const cpfSemMascara = cpf.replace(/\D/g, "");
            const cpfValido = validarCPF(cpfSemMascara);

            const cpfFormatado = aplicarMascara(cpf);
            event.target.value = cpfFormatado;

            if (cpfValido) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O CPF informado é inválido");  // CPF inválido
            }
        });
    }

    // Máscara de RG
    const rg = document.getElementById("rg");

    if (rg) {
        rg.addEventListener("input", function (event) {
            let rg = event.target.value;

            rg = rg.replace(/\D/g, "")
                .replace(/(\d{1})(\d{3})(\d{3})/, "$1.$2.$3");

            event.target.value = rg;
        });
    }


    // Máscara de telefone
    const telefone = document.getElementById("phone");

    if (telefone) {
        telefone.addEventListener("input", function (event) {
            let phone = event.target.value;


            phone = phone.replace(/\D/g, "")
                .replace(/(\d{2})(\d{4,5})(\d{4})/, "($1) $2-$3");

            event.target.value = phone;
        });
    }

    // Máscara de CEP
    const cep = document.getElementById("zip");

    if (cep) {
        cep.addEventListener("input", function (event) {
            let cep = event.target.value;

            cep = cep.replace(/\D/g, "")
                .replace(/(\d{5})(\d{3})/, "$1-$2");

            event.target.value = cep;
        });
    }

    // Máscara de placa de veículo
    const placa = document.getElementById("plate_vehicle");

    if (placa) {
        placa.addEventListener("input", function (event) {
            let plate = event.target.value;

            plate = plate.replace(/[^A-Za-z0-9]/g, "")
                .replace(/(\w{3})(\d{4})/, "$1-$2");

            event.target.value = plate.toUpperCase();
        });
    }

    // Mascara pra Quilometragem
    const km = document.getElementById("kms_vehicle");

    if (km) {
        km.addEventListener("input", function (event) {
            let kms = event.target.value;

            kms = kms.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = kms;
        });
    }

    // Mascara para formatar o preenchimento do preço
    const priceFormatterElements = document.getElementsByClassName("price_formatter");
    const price = document.getElementById("price");

    if (priceFormatterElements.length > 0) {
        Array.from(priceFormatterElements).forEach((element) => {
            element.addEventListener("input", function (event) {
                let value = event.target.value;
                value = value.replace(/\D/g, "");
                value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                event.target.value = "R$ " + value;
            });
        });
    }

    if (price) {
        price.addEventListener("input", function (event) {
            let price = event.target.value;

            price = price.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = "R$ " + price;
        });
    }

    // Carregamento de foto do formulário de cadastro
    const photoInput = document.getElementById("profilePhoto");

    if (photoInput) {
        photoInput.addEventListener("change", function (event) {
            const preview = document.getElementById("preview");
            if (preview) {
                preview.src = URL.createObjectURL(event.target.files[0]);
                preview.style.display = "block"; // Exibe a imagem de pré-visualização
            }
        });

        const preview = document.getElementById("preview");
        if (preview) {
            preview.addEventListener("click", function () {
                photoInput.click(); // Permite clicar na imagem para escolher novamente
            });
        }
    }

    // Desabilita o campo de endereço de entrega caso a opção de entrega seja "Não"
    const entregaSelect = document.getElementById("entregaSelect");

    if (entregaSelect) {
        entregaSelect.addEventListener("change", function () {
            const selectValue = this.value;
            const enderecoInput = document.getElementById("deliveryAdress");

            if (selectValue === "Não") {
                enderecoInput.disabled = true;
                enderecoInput.value = "Você selecionou a opção de retirada na loja";
            } else if (selectValue === "Sim") {
                enderecoInput.disabled = false;
                enderecoInput.value = "";
            }
        });
    }

    // Desabilita o campo de parcelas caso a opção de pagamento seja diferente de "Cartão de crédito"
    const paymentSelect = document.getElementById("paymentSelect");

    if (paymentSelect) {
        paymentSelect.addEventListener("change", function () {
            const selectValue = this.value;
            const parcelasInput = document.getElementById("parcelasAmount");

            if (selectValue === "cartão de crédito") {
                parcelasInput.disabled = false;
                parcelasInput.selectedIndex = -1;
            } else {
                parcelasInput.disabled = true;
                parcelasInput.selectedIndex = 0;
            }
        });
    }

    // Mostra o valor original do veiculo e já calcula o valor final com as parcelas
    const vehicleSelect = document.getElementById("vehicleSelect");
    const OriginalPriceInput = document.getElementById("OriginalPrice");

    if (vehicleSelect && OriginalPriceInput) {
        // Atualiza o preço quando o veículo for selecionado
        vehicleSelect.addEventListener("change", function () {
            // Obtém a opção selecionada
            const selectOption = vehicleSelect.options[vehicleSelect.selectedIndex];

            // Obtém o preço do veículo (do atributo data-price)
            const price = selectOption.getAttribute("data-price");

            // Preenche o campo de valor original (OriginalPrice) com o preço
            if (price) {
                OriginalPriceInput.value = price;  // O preço já vem formatado, então podemos simplesmente atribuí-lo
            }
        });
    }


    // Formulario de delete de veículos
    const deleteForms = document.querySelectorAll("form.delete-form");

    if (deleteForms.length > 0) {
        deleteForms.forEach((form) => {
            form.addEventListener("submit", function (event) {
                const confirmDelete = confirm("Tem certeza que deseja excluir este veículo?");
                if (!confirmDelete) {
                    event.preventDefault(); // Cancela a exclusão se o usuário cancelar
                }
            });
        });
    }

    // Formulário de envio de foto tela de configurações
    function submitPhotoForm() {
        var fileInput = document.getElementById("profilePhoto");
        
        // Verifica se um arquivo foi selecionado
        if (fileInput.files.length > 0) {
            var formData = new FormData();
            formData.append("profilePhoto", fileInput.files[0]);

            fetch("", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Foto de perfil atualizada com sucesso!");
                    // Atualiza a imagem exibida na tela após o upload, se necessário
                    const preview = document.getElementById("preview");
                    if (preview) {
                        preview.src = URL.createObjectURL(fileInput.files[0]);
                    }
                } else {
                    alert("Erro ao atualizar a foto.");
                }
            })
            .catch(error => {
                console.error("Erro:", error);
                alert("Erro ao enviar a foto.");
            });
        } else {
            alert("Por favor, selecione uma foto.");
        }
    }

    // Adiciona o ouvinte de evento para o botão "Enviar"
    const submitButton = document.querySelector("button[onclick='submitPhotoForm()']");
    if (submitButton) {
        submitButton.addEventListener("click", function (event) {
            event.preventDefault();  // Impede o envio do formulário completo
            submitPhotoForm();  // Chama a função para enviar apenas a foto
        });
    }

       
    // Console log para verificar o carregamento do arquivo JavaScript
    console.log("JavaScript carregado e DOM pronto!");
});
