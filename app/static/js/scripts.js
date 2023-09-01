$(document).ready(function() {
    const cadastroList = $('#cadastro-list');
    const toggleButton = $('#toggle-cadastros');

    toggleButton.click(function() {
        cadastroList.toggleClass('hidden');
    });
});
