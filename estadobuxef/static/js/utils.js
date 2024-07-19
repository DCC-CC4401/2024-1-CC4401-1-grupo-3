function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const changeState = (element, reporte) => {
    // get reporte containing element
    const local_parent = element.parentElement

    if (local_parent.classList.contains("active"))   {
        local_parent.classList.remove("active")
        location.reload()
    } else {
        local_parent.classList.add("active")
    }

    const parent = local_parent.parentElement
    const estado_element = parent.getElementsByClassName("reporte-estado")[0]

    // clean reporte status
    const estado_anterior = estado_element.innerText
    estado_element.innerText = ""

    // create new selectElement to replace with reporte status
    const selector = document.createElement("select")
    selector.classList.add("reporte-estado")

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