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
            console.log("Foto enviada");
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

});

document.addEventListener("DOMContentLoaded", function () {
    // Desabilita o campo de endereço de entrega caso a opção de entrega seja "Não"
    document.getElementById("entregaSelect").addEventListener("change", function () {
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

    // Desabilita o campo de parcelas caso a opção de pagamento seja diferente de "Cartão de crédito"
    document.getElementById("paymentSelect").addEventListener("change", function () {
        const selectValue = this.value;
        const parcelasInput = document.getElementById("parcelasAmount");

        // Verifica se a opção escolhida é "Cartão de Crédito"
        if (selectValue === "cartão de crédito") {
            parcelasInput.disabled = false;
            parcelasInput.selectedIndex = -1;
        } else {
            parcelasInput.disabled = true;
            parcelasInput.selectedIndex = 0;
        }
    });
});
