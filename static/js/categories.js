const headers = "Content-Type': 'application/json"

const newCategoryForm = document.getElementById('newCategoryForm')
const newCategoryInput = document.getElementById('newCategoryInput');

//Categories page ------------------------------------------------------------

const categoryTable = document.getElementById('category-table')
if (categoryTable) {
    categoryTable.querySelectorAll('#delete-category-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const id = this.getAttribute('data-id')

            if (confirm('Tem certeza que deseja remover esta categoria?')) {
                fetch(`/delete_category/${id}`, {
                    method: 'DELETE',
                    header: headers
                }).then(() => window.location.reload())
            }

        })
    })
}

