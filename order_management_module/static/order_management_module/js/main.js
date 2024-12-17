// Constantes

const btnAddItem = document.getElementById('btnAddItem');
const ordersPanel = document.getElementById('ordersPanel');
const idsUsed = []

// Funciones

function generateUniqueId(idsUsed) {
    let newID;
    do {
        newID = Math.random().toString(36).substring(2, 5);
    } while (idsUsed.includes(newID)); 
    return newID;
}


function createItem(idItem, parentContainer) {
    
    const newDiv = document.createElement('div');
    newDiv.classList.add('item-container'); 

    const btnDelete = document.createElement('button');
    btnDelete.textContent = 'Eliminar item'; 
    btnDelete.classList.add('btn', 'btn-danger'); 
    btnDelete.type = 'button'; // Asegurar que no sea tipo submit
    btnDelete.addEventListener('click', () => {
        newDiv.remove(); // Elimina el contenedor principal
    });

    // Inserción del HTML restante
    newDiv.innerHTML = `
        <div class="form-floating">
            <input type="text" class="form-control" id="description_${idItem}" name="description_${idItem}"
                placeholder="Descripción">
            <label for="description_${idItem}">Descripción</label>
        </div>
        <div class="form-floating">
            <textarea class="form-control" placeholder="Detalle / Observación" id="detail_${idItem}"
                name="detail_${idItem}"></textarea>
            <label for="detail_${idItem}">Detalle / Observación</label>
        </div>
        <div>
            <label for="images_${idItem}" class="form-label">Imágenes del ítem</label>
            <input class="form-control" type="file" id="images_${idItem}" name="images_${idItem}" multiple>
        </div>
    `;

    // Insertar el botón al inicio del contenedor
    newDiv.appendChild(btnDelete);

    // Agregar el nuevo elemento al contenedor padre
    parentContainer.appendChild(newDiv);
}


btnAddItem.addEventListener("click", () => {
    let last_id = generateUniqueId(idsUsed);
    idsUsed.push(last_id);
    createItem(last_id, ordersPanel);
});

