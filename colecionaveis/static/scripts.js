async function deletarItem(itemId) {
    const resposta = await fetch(`/deletar/${itemId}`, { method: 'DELETE' });
    if (resposta.ok) {
        document.getElementById(`item-${itemId}`).remove();
        alert('Item deletado com sucesso!');
    } else {
        alert('Falha ao deletar o item.');
    }
}

async function atualizarItem(event, itemId) {
    event.preventDefault();

    const nome = document.getElementById('atualizar-nome').value;
    const descricao = document.getElementById('atualizar-descricao').value;
    const categoria = document.getElementById('atualizar-categoria').value;

    const resposta = await fetch(`/atualizar/${itemId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, descricao, categoria })
    });

    if (resposta.ok) {
        const itemAtualizado = await resposta.json();
        const itemDiv = document.getElementById(`item-${itemId}`);
        itemDiv.innerHTML = `${itemAtualizado.nome} - ${itemAtualizado.descricao} - ${itemAtualizado.categoria}
                             <button onclick="mostrarFormularioDeAtualizacao(${itemId})">Atualizar</button>
                             <button onclick="deletarItem(${itemId})">Deletar</button>`;
        alert('Item atualizado com sucesso!');

        //ocultar o formulário após a atualização
        const formulario = document.getElementById(`formulario-atualizacao-${itemId}`);
        formulario.style.display = 'none';
    } else {
        alert('Falha ao atualizar o item.');
    }
}

function mostrarFormularioDeAtualizacao(itemId) {
    const formulario = document.getElementById(`formulario-atualizacao-${itemId}`);
    if (formulario) {
        formulario.style.display = formulario.style.display === 'none' ? 'block' : 'none';
    } else {
        console.error(`Formulário de atualização para o ID ${itemId} não encontrado.`);
    }
}