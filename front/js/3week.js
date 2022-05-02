const listing = () => {
  console.log('화면 로딩 후 실행')
}
const open_box = () => {
  const postBox = document.querySelector('#post-box')
  postBox.style.display = 'block'
}
const close_box = () => {
  const postBox = document.querySelector('#post-box')
  postBox.style.display = 'none'
}
const makeCardContent = (comment,desc,image,star,title) =>{
  let star_image = '*'.repeat(star)
  const cardContent = `<div class="col">
        <div class="card h-100">
          <img src="${image}"
               class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <p class="card-text">${desc}</p>
            <p>${star_image}</p>
            <p class="mycomment">${comment}</p>
          </div>
        </div>
      </div>`
  return cardContent
}
document.addEventListener("DOMContentLoaded", function () {
  $.ajax({
    type: "GET",
    url: "http://spartacodingclub.shop/web/api/movie",
    data: {},
    success(response) {
      const movies = response['movies']
      const cardBox =  document.getElementById('cards-box')
      for (let i = 0; i < movies.length; i++) {
        let {comment,desc,image,star,title} = movies[i]
        const cardItem = document.createElement('div')
        cardItem.innerHTML = makeCardContent(comment,desc,image,star,title)
        cardBox.appendChild(cardItem)
      }
    }
  })
})
