$(document).ready(function () {
  show_order();
});
const get_order = () =>{
  const name = document.querySelector('#name').value
  const address = document.querySelector('#address').value
  const size = document.querySelector('#size').value
  return {
    'name': name,
    'address': address,
    'size': size,
  };
}
const updateTableList = (data) =>{
  const tr = document.createElement('tr')
  const listItem = `
    <td>${data.name}</td>
    <td>${data.address}</td>
    <td>${data.size}</td>
  `
  tr.innerHTML = listItem
  return tr
}
function show_order() {
  $.ajax({
    type: 'GET',
    url: '/mars',
    data: {},
    success: function (response) {
      const orderListTable = document.querySelector('#orderListTable tbody')
      response.data.forEach((data)=>{
        orderListTable.append(updateTableList(data))

      })
    }
  });
}
function save_order() {
  $.ajax({
    type: 'POST',
    url: '/mars',
    data: get_order(),
    success: function (response) {
      window.location.reload()
    }
  });
}