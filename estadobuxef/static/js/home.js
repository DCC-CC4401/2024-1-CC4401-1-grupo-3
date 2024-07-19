

const toggleCategoryList = (element) => {
    categoryList = element.getElementsByTagName("ul")[0]
    if (categoryList.style.display === "none") {
        categoryList.style.display = "block"
        categoryList.style.animation = "categoryDropdown 0.5s ease-in-out"
    } else {
        categoryList.style.display = "none"

    }
}
