// new WOW().init();

// alert("Hello, World");

// Block to fetch data, get only the selected item, and show and hide respective view

const update_prod = (prod_id) => {
  // Show edit form and hide add form
  document.querySelector("#add_box").style.display = "none";
  document.querySelector("#edit_box").style.display = "block";

  var updt_id = prod_id;
  console.log(`this is the ${updt_id} updating function`);
  // Fetch data from db to get all products and send response only with selected product.
  fetch("responseJSON")
    .then((response) => response.json())
    .then((response) => {
      for (i = 0; i < response.length; i++) {
        let prod = response[i];
        if (prod.id === updt_id) {
          editProd_view(prod);
        }
      }
      console.log("response - ", response);
    });
};

// Block to populate textarea that allows user to update product info.

const editProd_view = (response) => {
  // Getting response with information only for product to be edited.
  console.log("response view- ", response);
  let edit_name = response.name;
  console.log("response name- ", response.name);
  let edit_price = response.price;
  console.log("response price- ", response.price);
  let edit_descpt = response.description;
  console.log("response descript- ", response.description);

  // Get all product information and populate the form to make a put request with updating info.
  let new_name = (document.querySelector(
    "#editProdName"
  ).innerHTML = edit_name);
  let new_price = (document.querySelector(
    "#editProdPrice"
  ).innerHTML = edit_price);
  let new_textarea = (document.querySelector(
    "#editProdDescpt"
  ).innerHTML = edit_descpt);

  saveUptProd(response);
};

// Block to send put request to the server and save updated product info.

const saveUptProd = (response) => {
  let product = response;
  let prod_id = response.id;

  // On submit, send product info to update product.
  // document.querySelector("#editProd_form").onsubmit = () => {
  //   // Get all values from textarea to update content.
  //   let new_prodName = document.getElementById("editProdName").value;
  //   let new_prodPrice = document.getElementById("editProdPrice").value;
  //   let new_prodDescpt = document.getElementById("editProdDescpt").value;
  // };

  console.log("new_content: ", product, prod_id);
};
