// Evento de validação de CPF
function validarCPF() {
    const cpf = document.getElementById("cpf").value.replace(/\D/g, "");
    const cpfValido = cpf.length === 11;

    if (cpfValido) {
        const cpfArray = Array.from(cpf);s
        let soma = 0;


        for (let i = 0; i < 9; i++) {
            soma += parseInt(cpfArray[i]) * (10 - i);
        }

        let resto = (soma * 10) % 11;
        let digitoVerificador = resto === 10 ? 0 : resto;

        if (digitoVerificador === parseInt(cpfArray[9])) {
            soma = 0;

            // Calcula o segundo dígito verificador
            for (let i = 0; i < 10; i++) {
                soma += parseInt(cpfArray[i]) * (11 - i);
            }

            resto = (soma * 10) % 11;
            digitoVerificador = resto === 10 ? 0 : resto;

            if (digitoVerificador === parseInt(cpfArray[10])) {
                return true;
            }
        }
    }

    return false;    
}

document.getElementById("cpf").addEventListener("input", function (event) {
    const cpf = event.target.value; 

    const cpfValido = validarCPF(cpf);

    if (cpfValido) {
        event.target.setCustomValidity("");
    } else {
        event.target.setCustomValidity("O CPF informado é inválido");
    }
});

// Mascara de CPF
document.getElementById("cpf").addEventListener("input", function (event) {
    const cpf = event.target.value.replace(/\D/g, "");
    const cpfFormatado = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");

    event.target.value = cpfFormatado;
});

// Evento de carregamento do submenu do usuário
document.addEventListener("DOMContentLoaded", function () {
    const userIcon = document.getElementById("user-icon");
    const userSubmenu = document.getElementById("user-submenu");

    
    userIcon.addEventListener("click", function (event) {
        event.preventDefault();
        userSubmenu.style.display = userSubmenu.style.display === "block" ? "none" : "block";
    });

    
    window.addEventListener("click", function (event) {
        if (!userIcon.contains(event.target) && !userSubmenu.contains(event.target)) {
            userSubmenu.style.display = "none";
        }
    });
});

// Evento de carregamento foto do formulário de cadastro
function previewImage(event) {
    const preview = document.getElementById('preview');
    preview.src = URL.createObjectURL(event.target.files[0]);
    preview.style.display = 'block';
}

// Evento de carregamento da consulta de cliente
document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const cpf = document.getElementById("cpf").value;
    
    fetch(`/search_customer?cpf=${cpf}`)
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
            
            
            resultContainer.style.display = "block";
        })
        .catch(error => {
            alert(error.message);
        });
    
});

// Evento de carregamento da consulta de veículo

document.getElementById("search-form-vehicle").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const placa = document.getElementById("placa").value;
    
    fetch(`/search_vehicle?placa=${placa}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Veículo não encontrado');
            }
        })
        .then(data => {
            
            const resultContainer = document.getElementById("result-container-vehicle");
            const vehiclePicture = document.getElementById("vehicle-picture");
            const vehicleDetails = document.getElementById("vehicle-details");
            
            vehiclePicture.innerHTML = `<img src="${data.fotovehicle}" alt="Foto do veiculo" style="width: 150px; height: auto;">`;
            
            vehicleDetails.innerHTML = `
                <p><strong>Marca:</strong> ${data.marca}</p>
                <p><strong>Modelo:</strong> ${data.modelo}</p>
                <p><strong>Ano:</strong> ${data.ano}</p>
                <p><strong>Cor:</strong> ${data.cor}</p>
                <p><strong>Preço:</strong> R$ ${data.preco}</p>
            `;
            
            
            resultContainer.style.display = "block";
        })
        .catch(error => {
            alert(error.message);
        });
    
});