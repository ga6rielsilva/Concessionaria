document.addEventListener("DOMContentLoaded", function () {
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

    // Carregamento da consulta de cliente ** PRECISA SER ALTERADO **
    const searchForm = document.getElementById("search-form");

    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const cpf = document.getElementById("cpf").value;

            // Simula a resposta do servidor
            const mockData = {
                fotoPerfil: "https://via.placeholder.com/150",
                nome: "João Silva",
                telefone: "(11) 98765-4321",
                email: "joao.silva@example.com",
                endereco: "Rua Fictícia, 123",
                cidade: "São Paulo",
                estado: "SP",
                pais: "Brasil"
            };

            // Simula o promesso do `fetch`
            Promise.resolve({ ok: true, json: () => Promise.resolve(mockData) })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Cliente não encontrado');
                    }
                })
                .then(data => {

                    const resultContainer = document.getElementById("result-container");
                    const profilePicture = document.getElementById("profile-picture");
                    const customerDetails = document.getElementById("customer-details");

                    profilePicture.innerHTML = `<img src="${data.fotoPerfil}" alt="Foto de Perfil" style="width: 150px; height: auto;">`;

                    customerDetails.innerHTML = `
                    <p><strong>Nome:</strong> ${data.nome}</p>
                    <p><strong>Telefone:</strong> ${data.telefone}</p>
                    <p><strong>Email:</strong> ${data.email}</p>
                    <p><strong>Endereço:</strong> ${data.endereco}</p>
                    <p><strong>Cidade:</strong> ${data.cidade}</p>
                    <p><strong>Estado:</strong> ${data.estado}</p>
                    <p><strong>País:</strong> ${data.pais}</p>
                `;

                    resultContainer.style.display = "grid";
                })
                .catch(error => {
                    alert(error.message);
                });
        });
    }

});


// // Evento de carregamento da consulta de cliente
// document.getElementById("search-form").addEventListener("submit", function (event) {
//     event.preventDefault();

//     const cpf = document.getElementById("cpf").value;

//     fetch(`/search_customer?cpf=${cpf}`)
//         .then(response => {
//             if (response.ok) {
//                 return response.json();
//             } else {
//                 throw new Error('Cliente não encontrado');
//             }
//         })
//         .then(data => {

//             const resultContainer = document.getElementById("result-container");
//             const profilePicture = document.getElementById("profile-picture");
//             const customerDetails = document.getElementById("customer-details");


//             profilePicture.innerHTML = `<img src="${data.fotoPerfil}" alt="Foto de Perfil" style="width: 150px; height: auto;">`;


//             customerDetails.innerHTML = `
//                 <p><strong>Nome:</strong> ${data.nome}</p>
//                 <p><strong>Telefone:</strong> ${data.telefone}</p>
//                 <p><strong>Email:</strong> ${data.email}</p>
//                 <p><strong>Endereço:</strong> ${data.endereco}</p>
//                 <p><strong>Cidade:</strong> ${data.cidade}</p>
//                 <p><strong>Estado:</strong> ${data.estado}</p>
//                 <p><strong>País:</strong> ${data.pais}</p>
//             `;


//             resultContainer.style.display = "block";
//         })
//         .catch(error => {
//             alert(error.message);
//         });

// });

// // Evento de carregamento da consulta de veículo

// document.getElementById("search-form-vehicle").addEventListener("submit", function (event) {
//     event.preventDefault();

//     const placa = document.getElementById("placa").value;

//     fetch(`/search_vehicle?placa=${placa}`)
//         .then(response => {
//             if (response.ok) {
//                 return response.json();
//             } else {
//                 throw new Error('Veículo não encontrado');
//             }
//         })
//         .then(data => {

//             const resultContainer = document.getElementById("result-container-vehicle");
//             const vehiclePicture = document.getElementById("vehicle-picture");
//             const vehicleDetails = document.getElementById("vehicle-details");

//             vehiclePicture.innerHTML = `<img src="${data.fotovehicle}" alt="Foto do veiculo" style="width: 150px; height: auto;">`;

//             vehicleDetails.innerHTML = `
//                 <p><strong>Marca:</strong> ${data.marca}</p>
//                 <p><strong>Modelo:</strong> ${data.modelo}</p>
//                 <p><strong>Ano:</strong> ${data.ano}</p>
//                 <p><strong>Cor:</strong> ${data.cor}</p>
//                 <p><strong>Preço:</strong> R$ ${data.preco}</p>
//             `;


//             resultContainer.style.display = "block";
//         })
//         .catch(error => {
//             alert(error.message);
//         });

// });