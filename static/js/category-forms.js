const categoryForm = document.getElementById('categoryForm')
const _name = document.getElementById('name');

categoryForm.addEventListener('submit', (event) => {
    if (_name.value.trim() == "") {
        alert("Por favor, preencha o nome da categoria!")
        event.preventDefault()
    }
})