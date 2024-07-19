const changeState = (element, reporte) => {
    // get reporte containing element
    const local_parent = element.parentElement
    const parent = local_parent.parentElement
    const estado_element = parent.getElementsByClassName("reporte-estado")[0]

    // clean reporte status
    const estado_anterior = estado_element.innerText
    estado_element.innerText = ""

    // create new selectElement to replace with reporte status
    const selector = document.createElement("select")

    // create optionElement for Pendiente
    const pendiente_option = document.createElement("option")
    pendiente_option.value = 'P'
    pendiente_option.text = "Pendiente"

    // create optionElement for Resuelto
    const resuelto_option = document.createElement("option")
    resuelto_option.value = 'R'
    resuelto_option.text = "Resuelto"

    // add options to selectElement
    if (estado_anterior === "Pendiente") {
        selector.options.add(pendiente_option)
        selector.options.add(resuelto_option)
    } else if (estado_anterior === "Resuelto") {
        selector.options.add(resuelto_option)
        selector.options.add(pendiente_option)
    }

    // replace reporte status with selectElement
    estado_element.appendChild(selector)
    // selector.value = ""

    selector.addEventListener("change", (ev) => {
        const data = {
            reporteId : reporte,
            reporteOldStatus : estado_anterior === 'Pendiente' || estado_anterior ==='P' ? 'P'  : 'R',
            reporteNewStatus : selector.value === 'Pendiente' || selector.value === 'P' ? 'P' : 'R'
        }
        const csrftoken = getCookie('csrftoken');
        if (data.reporteOldStatus !== data.reporteNewStatus) {
            fetch(location + "/update-report", {
                headers: {
                    "X-CSRFToken" : csrftoken
                },
                method: 'POST',
                body: JSON.stringify(data)
            }).catch(error => {
                console.log(error)
            }).finally(() => {
                location.reload()
            })
        }
        // location.reload()
    })

}

const toggleCategoryList = (element) => {
    categoryList = element.getElementsByTagName("ul")[0]
    if (categoryList.style.display === "none") {
        categoryList.style.display = "block"
        categoryList.style.animation = "categoryDropdown 0.5s ease-in-out"
    } else {
        categoryList.style.display = "none"

    }
}
