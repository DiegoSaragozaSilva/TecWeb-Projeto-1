function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function changeText(div) {
  childrens = div.children;
  title = childrens[1].textContent;
  content = childrens[2].children[0].textContent;

  document.getElementsByClassName("form-card-title")[0].value = title;
  document.getElementsByClassName("autoresize")[0].value = content;
  document.getElementsByClassName("btn")[0].innerHTML = "Salvar"
  document.getElementsByClassName("post-type")[0].value = "edit"
  document.getElementsByClassName("org")[0].value = title
  document.getElementsByClassName("org")[1].value = content
}

function deleteNote(img) {
  div = img.parentElement
  childrens = div.children
  title = childrens[1].textContent;
  content = childrens[2].children[0].textContent;

  document.getElementsByClassName("form-card-title")[0].value = '';
  document.getElementsByClassName("autoresize")[0].value = '';
  document.getElementsByClassName("btn")[0].innerHTML = "Criar"
  document.getElementsByClassName("post-type")[0].value = "delete"
  document.getElementsByClassName("org")[0].value = title
  document.getElementsByClassName("org")[1].value = content

  document.getElementsByClassName('form-card')[0].submit();
}

function clearForm() {
  document.getElementsByClassName("form-card-title")[0].value = '';
  document.getElementsByClassName("autoresize")[0].value = '';
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  
  clearForm();

  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});
