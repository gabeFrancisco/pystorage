const productForm = document.getElementById('productForm')

const _name = document.getElementById('name')
const description = document.getElementById('description')
const quantity = document.getElementById('quantity')
const price = document.getElementById('price')
const categoryId = document.getElementById('category')

productForm.addEventListener('submit', (event) => {
    if (_name.value.trim() == "") {
        alert("Nome obrigatório!")
        event.preventDefault()
        return
    }

    if (description.value.trim() == "") {
        alert("Descrição é obrigatória!")
        event.preventDefault()
        return
    }

    if (quantity.value.trim() == "") {
        alert("Quantidade deve ser maior que 0!")
        event.preventDefault()
        return
    }

    if (price.value.trim() == "") {
        alert("Preço deve ser maior que 0!")
        event.preventDefault()
        return
    }
})