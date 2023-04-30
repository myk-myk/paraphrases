function saveValue(inputElement) {
    if (!inputElement) throw new Error('inputElement param is required');
    const {id, value} = inputElement;
    if (!id) throw new Error('inputElement should have an id attribute');
    localStorage.setItem(id, value);
}
function getSavedValue(inputElement) {
    if (!inputElement) throw new Error('inputElement param is required');
    const { id } = inputElement;
    if (!id) throw new Error('inputElemend should have an id attribute');
    const value = localStorage.getItem(id);
    return value;
}
const textarea = document.querySelector('#input_tree');
textarea.addEventListener("keyup", function(event) {
    saveValue(event.target)
});
const value = getSavedValue(textarea);
window.addEventListener('load', function() {
    textarea.value = value;
})
const button = document.querySelector('#reset_button');
button.addEventListener('click', function () {
    const { id } = textarea;
    localStorage.setItem(id, "");
})
