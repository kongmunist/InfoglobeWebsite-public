
function init() {
  var form = document.getElementById("msg_form");
  form.addEventListener('submit', handleForm);
}

function handleForm(event) {
  event.preventDefault();
  const form = document.getElementById("msg_form");
  const formData = new FormData(form)
  const data = JSON.stringify(formData.get('msg'));
  const recents = document.getElementById("recent_msg")
  recents.innerHTML = ""
  fetch('/savemessage', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: data,
  })
  .then(response => response.json())
  .then(json => json.forEach((item, i) => {
      const li = document.createElement("li")
      li.innerHTML = item
      recents.appendChild(li)
  }));

  form.reset()
}


window.onload = init
