
const carrito = new Map();

document.querySelectorAll('.agregar-carrito').forEach(boton => {
    boton.addEventListener('click', () => {
        const id = boton.dataset.id;
        const nombre = boton.dataset.nombre;
        const precio = Number(boton.dataset.precio);

        if (!Number.isFinite(precio) || precio < 0) {
            return;
        }

        if (carrito.has(id)) {
            carrito.get(id).cantidad++;
        } else {
            carrito.set(id, {
                nombre,
                precio,
                cantidad: 1
            });
        }

        actualizarCarrito();
    });
});

function actualizarCarrito() {
    const lista = document.getElementById('lista-carrito');
    const contador = document.getElementById('contador-carrito');
    const totalElemento = document.getElementById('total-carrito');

    lista.replaceChildren();

    let cantidadTotal = 0;
    let total = 0;

    if (carrito.size === 0) {
        const mensaje = document.createElement('p');
        mensaje.className = 'text-muted small';
        mensaje.textContent = 'Tu carrito está vacío.';
        lista.appendChild(mensaje);
    }

    carrito.forEach((producto, id) => {
        cantidadTotal += producto.cantidad;
        total += producto.precio * producto.cantidad;

        const fila = document.createElement('div');
        fila.className =
            'd-flex justify-content-between align-items-center gap-2 mb-2';

        const detalle = document.createElement('div');

        const nombre = document.createElement('div');
        nombre.className = 'fw-semibold small';
        nombre.textContent = producto.nombre;

        const precio = document.createElement('div');
        precio.className = 'text-muted small';
        precio.textContent =
            `${producto.cantidad} × $${producto.precio.toFixed(2)}`;

        detalle.append(nombre, precio);

        const eliminar = document.createElement('button');
        eliminar.type = 'button';
        eliminar.className = 'btn btn-outline-danger btn-sm';
        eliminar.textContent = '×';
        eliminar.setAttribute('aria-label', 'Eliminar producto');

        eliminar.addEventListener('click', () => {
            carrito.delete(id);
            actualizarCarrito();
        });

        fila.append(detalle, eliminar);
        lista.appendChild(fila);
    });

    contador.textContent = cantidadTotal;
    totalElemento.textContent = `$${total.toFixed(2)}`;
}
