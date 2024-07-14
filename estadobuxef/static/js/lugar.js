const likePlace = (element, lugar) => {
    const csrftoken = getCookie("csrftoken")
    const data = {
        lugar: lugar,
        likes: !!element.style.content
    }
    fetch("/like-place", {
        headers: {
            "X-CSRFToken": csrftoken,
        },
        method: "POST",
        body: JSON.stringify(data)
    }).catch(error => {
        console.log(error)
    }).then((response) => {
        if (response.statusText === "OK") {
            location.reload()
        }
    })
}