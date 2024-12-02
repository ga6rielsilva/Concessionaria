document.addEventListener("DOMContentLoaded", function () {
    // Validação do CPF e máscara
    // Seleciona o campo de CPF pelo ID
    const cpfok = document.getElementById("cpf");

    if (cpfok) {
        // Função para validar o CPF
        function validarCPF(cpf) {
            // Remove caracteres não numéricos
            const cpfNumeros = cpf.replace(/\D/g, "");
            // Verifica se o CPF tem 11 dígitos
            if (cpfNumeros.length !== 11) return false;

            const cpfArray = Array.from(cpfNumeros);
            let soma = 0;

            // Calcula o primeiro dígito verificador
            for (let i = 0; i < 9; i++) {
                soma += parseInt(cpfArray[i]) * (10 - i);
            }

            let resto = (soma * 10) % 11;
            let digitoVerificador = resto === 10 ? 0 : resto;

            // Verifica o primeiro dígito verificador
            if (digitoVerificador !== parseInt(cpfArray[9])) return false;

            soma = 0;

            // Calcula o segundo dígito verificador
            for (let i = 0; i < 10; i++) {
                soma += parseInt(cpfArray[i]) * (11 - i);
            }

            resto = (soma * 10) % 11;
            digitoVerificador = resto === 10 ? 0 : resto;

            // Verifica o segundo dígito verificador
            return digitoVerificador === parseInt(cpfArray[10]);
        }

        // Função para aplicar a máscara de CPF
        function aplicarMascara(cpf) {
            return cpf.replace(/\D/g, "")
                .replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
        }

        cpfok.addEventListener("input", function (event) {
            let cpf = event.target.value;

            // Remove a máscara do CPF
            const cpfSemMascara = cpf.replace(/\D/g, "")

            const cpfValido = validarCPF(cpfSemMascara);

            // Aplica a máscara ao CPF
            const cpfFormatado = aplicarMascara(cpf);
            event.target.value = cpfFormatado;

            // Define a mensagem de erro se o CPF for inválido
            if (cpfValido) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O CPF informado é inválido");
            }
        });
    }

    // Máscara de RG
    const rg = document.getElementById("rg");

    if (rg) {
        // Define o comprimento máximo do campo de RG
        rg.setAttribute("maxlength", "12");

        // Função para validar o RG
        function validarRG(rg) {
            const rgNumbers = rg.replace(/\D/g, "");
            return rgNumbers.length === 9;
        }

        rg.addEventListener("input", function (event) {
            let rg = event.target.value;

            // Remove caracteres não numéricos e aplica a máscara de RG
            rg = rg.replace(/\D/g, "")
                .replace(/(\d{2})(\d{3})(\d{3})(\d{1})/, "$1.$2.$3-$4");

            event.target.value = rg;

            // Define a mensagem de erro se o RG for inválido
            if (validarRG(rg)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O RG informado é inválido");
            }
        });
    }

    // Máscara de telefone
    const telefone = document.getElementById("phone");

    if (telefone) {
        // Define o comprimento máximo do campo de telefone
        telefone.setAttribute("maxlength", "15");

        // Função para validar o telefone
        function validarTelefone(phone) {
            // Remove caracteres não numéricos
            const phoneNumeros = phone.replace(/\D/g, "");
            // Verifica se o telefone tem entre 10 e 11 dígitos
            return phoneNumeros.length >= 10 && phoneNumeros.length <= 11;
        }

        telefone.addEventListener("input", function (event) {
            let phone = event.target.value;

            // Remove caracteres não numéricos e aplica a máscara de telefone
            phone = phone.replace(/\D/g, "")
                .replace(/(\d{2})(\d{4,5})(\d{4})/, "($1) $2-$3");

            // Atualiza o valor do campo de telefone com a máscara aplicada
            event.target.value = phone;

            // Valida o telefone e define a mensagem de erro se for inválido
            if (validarTelefone(phone)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O telefone informado é inválido");
            }
        });
    }

    // Máscara de CEP
    const cep = document.getElementById("zip");

    if (cep) {
        // Função para validar o CEP
        function validarCEP(cep) {
            const cepNumeros = cep.replace(/\D/g, "");
            return cepNumeros.length === 8;
        }

        cep.addEventListener("input", function (event) {
            let cep = event.target.value;

            // Remove caracteres não numéricos e aplica a máscara de CEP
            cep = cep.replace(/\D/g, "").substring(0, 8)
                .replace(/(\d{5})(\d{3})/, "$1-$2");

            event.target.value = cep;

            // Define a mensagem de erro se o CEP for inválido
            if (validarCEP(cep)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O CEP informado é inválido");
            }
        });
    }

    // Máscara de placa de veículo
    const placa = document.getElementById("plate_vehicle");

    if (placa) {
        // Define o comprimento máximo do campo de placa
        placa.setAttribute("maxlength", "8");

        placa.addEventListener("input", function (event) {
            let plate = event.target.value;

            // Remove caracteres não alfanuméricos
            plate = plate.replace(/[^A-Za-z0-9]/g, "");

            // Verifica se o quinto dígito é uma letra ou um número
            if (plate.length > 4 && isNaN(plate[4])) {
                placa.setAttribute("maxlength", "7");
                // Padrão Mercosul: LLLNLNN
                plate = plate.replace(/(\w{3})(\w{1})(\w{1})(\w{2})/, "$1$2$3$4");
            } else {
                // Padrão antigo: LLL-9999
                plate = plate.replace(/(\w{3})(\w{4})/, "$1-$2");
            }

            event.target.value = plate.toUpperCase();
        });
    }

    // Máscara para quilometragem
    const km = document.getElementById("kms_vehicle");

    if (km) {
        km.addEventListener("input", function (event) {
            let kms = event.target.value;

            // Remove caracteres não numéricos e aplica a máscara de quilometragem
            kms = kms.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = kms;
        });
    }

    // Máscara para formatar o preenchimento do preço
    const priceFormatterElements = document.getElementsByClassName("price_formatter");
    const price = document.getElementById("price");

    if (priceFormatterElements.length > 0) {
        // Aplica a lógica abaixo a todos os elementos html com a classe "price_formatter"
        Array.from(priceFormatterElements).forEach((element) => {
            element.addEventListener("input", function (event) {
                let value = event.target.value;
                // Remove caracteres não numéricos e aplica a máscara de preço
                value = value.replace(/\D/g, "");
                value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                event.target.value = "R$ " + value;
            });
        });
    }

    if (price) {
        price.addEventListener("input", function (event) {
            let price = event.target.value;

            // Remove caracteres não numéricos e aplica a máscara de preço
            price = price.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = "R$ " + price;
        });
    }

    // Validação do Renavam
    const renavam = document.getElementById("renavam_vehicle");

    if (renavam) {
        // Define o comprimento máximo do campo de Renavam
        renavam.setAttribute("maxlength", "11");

        // Função para validar o Renavam
        function validarRenavam(renavam) {
            const renavamNumbers = renavam.replace(/\D/g, "");
            return renavamNumbers.length === 11;
        }

        renavam.addEventListener("input", function (event) {
            let renavam = event.target.value;

            // Remove caracteres não numéricos
            renavam = renavam.replace(/\D/g, "");

            event.target.value = renavam;

            // Define a mensagem de erro se o Renavam for inválido
            if (validarRenavam(renavam)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O Renavam informado é inválido");
            }
        });
    }

    // Validação do Chassi
    const chassi = document.getElementById("chassi_vehicle");

    if (chassi) {
        // Define o comprimento máximo do campo de Chassi
        chassi.setAttribute("maxlength", "17");

        // Função para validar o Chassi
        function validarChassi(chassi) {
            const chassiNumbers = chassi.replace(/[^A-Za-z0-9]/g, "");
            return chassiNumbers.length === 17;
        }

        chassi.addEventListener("input", function (event) {
            let chassi = event.target.value;

            // Remove caracteres não alfanuméricos
            chassi = chassi.replace(/[^A-Za-z0-9]/g, "");

            event.target.value = chassi.toUpperCase();

            // Define a mensagem de erro se o Chassi for inválido
            if (validarChassi(chassi)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O Chassi informado é inválido");
            }
        });
    }
});