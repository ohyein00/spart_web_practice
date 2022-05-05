$(document).ready(function () {
  show_bucket()
});
const get_bucket = () => {
  const bucket = document.querySelector('#bucket').value
  return {
    'bucket': bucket,
  };
}
const checkComplete = (id, content, complete) => {
  if (complete === 0) {
    return `
      <li>
      <h2>✅ ${content}</h2>
      <button onclick="done_bucket(${id})" type="button" class="btn btn-outline-primary">완료</button>    
      <button onclick="delete_bucket(${id})" type="button" class="btn">❌</button>
      </li>
    `
  } else {
    return `
      <li>
      <h2 class="done">✅ ${content}</h2>
      <button onclick="done_bucket(${id})" type="button" class="btn btn-outline-danger">취소</button>
      <button onclick="delete_bucket(${id})" type="button" class="btn">❌</button>
      </li>
    `
  }
}

function show_bucket() {
  $.ajax({
    type: "GET",
    url: "/bucket",
    data: {},
    success: function (response) {
      const list = document.querySelector('#bucket-list')
      let content = ''
      for(let i=0; i<response.data.length; i++){
        const item = response.data[i]
        content += checkComplete(item['id'], item['bucket'], item['complete'])
      }
      list.innerHTML = content
    }
  });
}

function save_bucket() {
  $.ajax({
    type: "POST",
    url: "/bucket",
    data: get_bucket(),
    success: function (response) {
    }
  });
  window.location.reload()
}

function done_bucket(id) {
  $.ajax({
    type: "POST",
    url: "/bucket/done",
    data: {'id': id},
    success: function (response) {
    }
  })
  window.location.reload()
}

function delete_bucket(id) {
  $.ajax({
    type: "POST",
    url: "/bucket/delete",
    data: {'id': id},
    success: function (response) {
    }
  })
  window.location.reload()
}