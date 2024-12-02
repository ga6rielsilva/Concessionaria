document.addEventListener("DOMContentLoaded", function () {
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
    const rgInput = document.getElementById("rg");
    if (rgInput) {
        function validarRG(rg) {
            const rgNumbers = rg.replace(/\D/g, "");
    
            return rgNumbers.length >= 5 && rgNumbers.length <= 14;
        }
    
        rgInput.addEventListener("input", function (event) {
            let rg = event.target.value;
    
            rg = rg.replace(/\D/g, "");
    
            if (rg.length === 7) {
                rg = rg.replace(/^(\d{1})(\d{3})(\d{3})$/, "$1.$2.$3");
            } else if (rg.length === 8) {
                rg = rg.replace(/^(\d{2})(\d{3})(\d{3})$/, "$1.$2.$3");
            } else if (rg.length === 9) {
                rg = rg.replace(/^(\d{2})(\d{3})(\d{3})(\d{1})$/, "$1.$2.$3-$4");
            } else if (rg.length > 5) {
                rg = rg.replace(/^(\d{1,2})(\d{3})(\d{1,4})$/, "$1.$2.$3");
            } else {
                rg = rg.replace(/^(\d{1,2})(\d{3})?$/, (_, p1, p2) => p2 ? `${p1}.${p2}` : p1);
            }
    
            event.target.value = rg;
    
            if (validarRG(rg.replace(/\D/g, ""))) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O RG informado é inválido.");
            }
        });
    
        rgInput.addEventListener("keydown", function (event) {
            if (event.key === "Backspace") {
                let cursorPosition = rgInput.selectionStart;
                let value = rgInput.value;
    
    
                if (cursorPosition > 0 && value[cursorPosition - 1].match(/[.\- ]/)) {
                    rgInput.setSelectionRange(cursorPosition - 1, cursorPosition - 1);
                    event.preventDefault(); // Previne comportamento padrão do backspace
                }
            }
        });
    }

    // Máscara de telefone
    const telefone = document.getElementById("phone");
    if (telefone) {
        telefone.setAttribute("maxlength", "15");

        function validarTelefone(phone) {
            const phoneNumeros = phone.replace(/\D/g, "");
            return phoneNumeros.length >= 10 && phoneNumeros.length <= 11;
        }

        telefone.addEventListener("input", function (event) {
            let phone = event.target.value;

            phone = phone.replace(/\D/g, "")
                .replace(/(\d{2})(\d{4,5})(\d{4})/, "($1) $2-$3");

            event.target.value = phone;

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
        function validarCEP(cep) {
            const cepNumeros = cep.replace(/\D/g, "");
            return cepNumeros.length === 8;
        }

        cep.addEventListener("input", function (event) {
            let cep = event.target.value;

            cep = cep.replace(/\D/g, "").substring(0, 8)
                .replace(/(\d{5})(\d{3})/, "$1-$2");

            event.target.value = cep;

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
        placa.setAttribute("maxlength", "7");

        placa.addEventListener("input", function (event) {
            let plate = event.target.value;

            plate = plate.replace(/[^A-Za-z0-9]/g, "")
                .replace(/(\w{3})(\w{1})(\w{1})(\w{2})/, "$1$2-$3$4");

            event.target.value = plate.toUpperCase();
        });
    }

    // Máscara para quilometragem
    const km = document.getElementById("kms_vehicle");
    if (km) {
        km.addEventListener("input", function (event) {
            let kms = event.target.value;

            kms = kms.replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            event.target.value = kms;
        });
    }

    // Máscara para formatar o preenchimento do preço
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

    // Validação do Renavam
    const renavam = document.getElementById("renavam_vehicle");
    if (renavam) {
        renavam.setAttribute("maxlength", "11");

        function validarRenavam(renavam) {
            const renavamNumbers = renavam.replace(/\D/g, "");
            return renavamNumbers.length === 11;
        }

        renavam.addEventListener("input", function (event) {
            let renavam = event.target.value;

            renavam = renavam.replace(/\D/g, "");

            event.target.value = renavam;

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
        chassi.setAttribute("maxlength", "17");

        function validarChassi(chassi) {
            const chassiNumbers = chassi.replace(/[^A-Za-z0-9]/g, "");
            return chassiNumbers.length === 17;
        }

        chassi.addEventListener("input", function (event) {
            let chassi = event.target.value;

            chassi = chassi.replace(/[^A-Za-z0-9]/g, "");

            event.target.value = chassi.toUpperCase();

            if (validarChassi(chassi)) {
                event.target.setCustomValidity("");
            } else {
                event.target.setCustomValidity("O Chassi informado é inválido");
            }
        });
    }

    // Verificação de carregamento dos script
    console.log("Validator.js carregado com sucesso!");
});