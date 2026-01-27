let showState = true

const cash = document.getElementById('cash')
const show_cash_b = document.getElementById('show-cash-b')

show_cash_b.onclick = function () {
    if (showState) {
        cash.innerHTML = "R$********"
    }
    else {
        cash.innerHTML = "R$3.127,72"
    }

    showState = !showState
}
