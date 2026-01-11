document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    alert(`You clicked on ${card.textContent}`);
  });

});
// Fetch restaurant data
fetch("restaurants.json")
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById("restaurant-list");
    list.innerHTML = "";

    data.forEach(rest => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <img src="${rest.image}" alt="${rest.name}" class="card-img">
        <h3>${rest.name}</h3>
        <p>${rest.cuisine}</p>
        <p>⭐ ${rest.rating} | ${rest.price}</p>
      `;
      list.appendChild(card);
    });
  })
  .catch(err => console.error(err));
