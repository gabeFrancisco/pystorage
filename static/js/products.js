//Product table modal logic---------------------------------------------------

const closeModal = document.getElementById('close-modal');
const modal = document.getElementById('modal-container');

const productTable = document.getElementById('product-table')
if (productTable) {
    productTable.querySelectorAll('.product-row').forEach(row => {
        row.addEventListener('click', function () {
            const id = this.cells[0].innerText;
            const name = this.cells[1].innerText;
            const description = this.cells[2].innerText;
            const quantity = this.cells[3].innerText;
            const price = this.cells[4].innerText;
            const category = this.cells[5].innerText;

            document.getElementById('product-id').innerText = id
            document.getElementById('product-name').innerText = name;
            document.getElementById('product-description').innerText = description;
            document.getElementById('product-quantity').innerText = quantity;
            document.getElementById('product-price').innerText = price;
            document.getElementById('product-category').innerText = category;

            modal.style.display = "block"
        })
    })
}

closeModal.onclick = function () {
    modal.style.display = "none";
}



