let newCategoryForm = document.getElementById('newCategoryForm')
let newCategoryInput = document.getElementById('newCategoryInput');

newCategoryForm.addEventListener('submit', (event) => {
    if (newCategoryInput.value.trim() == "") {
        alert("Por favor, preencha o nome da categoria!")
        event.preventDefault()
    }
})


