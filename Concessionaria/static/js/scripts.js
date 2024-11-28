document.addEventListener("DOMContentLoaded", function () {

    // Traduzindo placeholder {Ydate}
    const YdatePlaceholder = document.getElementById("Ydate");
        if (YdatePlaceholder) {
            const date = new Date();
            YdatePlaceholder.innerHTML ="&nbsp;" + date.getFullYear() + "&nbsp;";
        }
        
    // Traduzindo placeholder {username}
    const usernamePlaceholder = document.getElementById("username");
        if (usernamePlaceholder) {
            const date = new Date();
            usernamePlaceholder.innerHTML ="&nbsp;" + date.getFullYear() + "&nbsp;";
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

    // Mascara pra Preço do veículo
    const price = document.getElementById("price_vehicle");

    if (price) {
        price.addEventListener("input", function (event) {
            let price = event.target.value;

            price = price.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = "R$ " + price;
        });
    }

    // Carregamento de foto do formulário de cadastro
    const photoInput = document.getElementById("profilePhoto" || "vehiclePhoto");

    if (photoInput) {
        photoInput.addEventListener("change", function (event) {
            const preview = document.getElementById("preview");
            preview.src = URL.createObjectURL(event.target.files[0]);
            preview.style.display = "block";
        });
    }
});