// new WOW().init();

document.addEventListener("DOMContentLoaded", function () {
  document
    .querySelector("#delete_prod")
    .addEventListener("click", () => delete_prod(prod_id));
});

const delete_prod = (prod_id) => {
  let prod_selected = prod_id;
  console.log("this is the product id", prod_selected);
};

// const loadProducts = () => {
//   // Fetch data from db to get all products
//   fetch("responseJSON")
//     .then((response) => response.json())
//     .then((response) => {
//       console.log("response - ", response);
//     });
// };
