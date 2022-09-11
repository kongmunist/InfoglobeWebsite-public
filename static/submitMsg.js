
function init() {
  var form = document.getElementById("msg_form");
  form.addEventListener('submit', handleForm);
}

function handleForm(event) {
  event.preventDefault();
  const form = document.getElementById("msg_form");
  const formData = new FormData(form)
  const msg = formData.get('msg')
  const data = JSON.stringify(msg);
  const recents = document.getElementById("recent_msg")

  fetch('/savemessage', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: data,
  })

  const li = document.createElement("li")
  li.innerHTML = msg
  recents.prepend(li)
  recents.lastElementChild.remove()
  form.reset()
}


window.onload = init
