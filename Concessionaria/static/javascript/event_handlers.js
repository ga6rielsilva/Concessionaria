document.addEventListener("DOMContentLoaded", function () {
    // Carregamento de foto do formulário de cadastro
    const photoInput = document.getElementById("profilePhoto");
    if (photoInput) {
        photoInput.addEventListener("change", function (event) {
            const preview = document.getElementById("preview");
            if (preview) {
                preview.src = URL.createObjectURL(event.target.files[0]);
                // Exibe a imagem de pré-visualização
                preview.style.display = "block";
            }
        });

        const preview = document.getElementById("preview");
        if (preview) {
            preview.addEventListener("click", function () {
                // Permite clicar na imagem para escolher novamente
                photoInput.click();
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
                ParcelasPriceInput.value = "R$ 0,00";
                valorTotal.value = vehicleSelector.options[vehicleSelector.selectedIndex].getAttribute("data-price").toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
            }
        });
    }

    // Mostra o valor original do veiculo e já calcula o valor final com as parcelas
    const vehicleSelector = document.getElementById("vehicle-selector");
    const originalPriceInput = document.getElementById("OriginalPrice");

    // Atualizar o valor original ao selecionar um veículo
    if (vehicleSelector && originalPriceInput) {
        vehicleSelector.addEventListener("change", function () {
            const selectedOption = vehicleSelector.options[vehicleSelector.selectedIndex];
            const price = selectedOption.getAttribute("data-price");

            // Formatar e exibir o valor
            if (price) {
                originalPriceInput.value = price.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
            } else {
                originalPriceInput.value = "R$ 0,00";
            }
        });
    }

    // Atualizar o valor final ao selecionar o número de parcelas
    const parcelasInput = document.getElementById("parcelasAmount");
    const ParcelasPriceInput = document.getElementById("ParcelasPrice");
    const valorTotal = document.getElementById("valorTotal");

    if (parcelasInput && ParcelasPriceInput && originalPriceInput && valorTotal) {
        parcelasInput.addEventListener("change", function () {
            const selectedOption = parcelasInput.options[parcelasInput.selectedIndex];
            const parcelas = selectedOption.value;


            const price = originalPriceInput.value.replace(/\D/g, "");
            const interestRate = 0.12;
            const TotalPrice = price * Math.pow(1 + interestRate, parcelas / 12);
            const ParcelasPrice = TotalPrice / parcelas;


            // Formatar e exibir o valor
            ParcelasPriceInput.value = ParcelasPrice.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
            valorTotal.value = TotalPrice.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
        });
    }

    // Formulario de delete de veículos
    const deleteVehicleForms = document.querySelectorAll("form.delete-form");

    if (deleteVehicleForms.length > 0) {
        deleteVehicleForms.forEach((form) => {
            form.addEventListener("submit", function (event) {
                const confirmDelete = confirm("Tem certeza que deseja excluir este veículo?");
                if (!confirmDelete) {
                    // Cancela a exclusão se o usuário cancelar
                    event.preventDefault();
                }
            });
        });
    }

    // Formulario de delete de cliente
    const deleteCustomersForms = document.querySelectorAll("form.delete-Customers-form");

    if (deleteCustomersForms.length > 0) {
        deleteCustomersForms.forEach((form) => {
            form.addEventListener("submit", function (event) {
                const confirmDelete = confirm("Tem certeza que deseja excluir este cliente?");
                if (!confirmDelete) {
                    // Cancela a exclusão se o usuário cancelar
                    event.preventDefault();
                }
            });
        });
    }

    // Confirmação de venda
    const confirmSaleForms = document.getElementById("vehicle-selector");
    const hiddenInput = document.getElementById("selectedVehicleId");

    if (confirmSaleForms && hiddenInput) {
        confirmSaleForms.addEventListener("change", function () {
            // Pegando o ID do veículo selecionado
            const selectedVehicle = this.value;
            // Atualizando o campo oculto com o ID do veículo
            hiddenInput.value = selectedVehicle;
            console.log("Veículo selecionado: ", selectedVehicle);

        });
    }
});