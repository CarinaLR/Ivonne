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
    });
};

// Block to populate textarea that allows user to update product info.

const editProd_view = (response) => {
  // Getting response with information only for product to be edited.
  let prod_id = response.id;
  console.log("response view- ", response);
  let edit_name = response.name;
  console.log("response name- ", response.name);
  let edit_price = response.price;
  console.log("response price- ", response.price);
  let edit_descpt = response.description;
  console.log("response descript- ", response.description);

  // Get all product information and populate the form to make a put request with updating info.
  let prod_idUpt = (document.querySelector("#prod_idUpt").innerHTML = prod_id);
  let new_name = (document.querySelector(
    "#editProdName"
  ).innerHTML = edit_name);
  console.log("change1 ", new_name);
  let new_price = (document.querySelector(
    "#editProdPrice"
  ).innerHTML = edit_price);
  console.log("change2 ", new_price);
  let new_textarea = (document.querySelector(
    "#editProdDescpt"
  ).innerHTML = edit_descpt);
  console.log("change3 ", new_textarea);

  // saveUptProd(response.id);
  let id = prod_id;
  console.log("id:", id);
  let upt_prodName, upt_prodPrice, upt_prodDescpt;
  //On submit, send product info to update product.
  document.querySelector("#editProd_form").onsubmit = () => {
    // Get all values from textarea to update content.
    upt_prodName = document.getElementById("editProdName").value;
    new_prodPrice = document.getElementById("editProdPrice").value;
    new_prodDescpt = document.getElementById("editProdDescpt").value;

    fetch(`/editProduct/${id}`, {
      method: "PUT",
      body: JSON.stringify({
        name: upt_prodName,
        description: upt_prodDescpt,
        price: upt_prodPrice,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("result ->", result);
      });

    console.log(
      `ID: ${id}, Name: ${upt_prodName}, Price: ${upt_prodPrice}, Description: ${upt_prodDescpt}`
    );
    //Once the post has been submitted, return false to prevent reload.
    return false;
  };
};

// Block to send put request to the server and save updated product info.

// const saveUptProd = () => {
//   let new_prodName, new_prodPrice, new_prodDescpt;
//   let prod_id = document.getElementById("prod_idUpt").value;
//   console.log("id:", prod_id);
//   let id = parseInt(prod_id);
//   console.log("id:", id);
//   //On submit, send product info to update product.
//   document.querySelector("#editProd_form").onsubmit = () => {
//     // Get all values from textarea to update content.
//     new_prodName = document.getElementById("editProdName").value;
//     new_prodPrice = document.getElementById("editProdPrice").value;
//     new_prodDescpt = document.getElementById("editProdDescpt").value;

//     // fetch(`/editProduct/${prod_id}`, {
//     //   method: "PUT",
//     //   body: JSON.stringify({
//     //     name: new_content,
//     //     description: new_prodDescpt,
//     //     price: new_prodPrice,
//     //   }),
//     // })
//     //   .then((response) => response.json())
//     //   .then((result) => {
//     //     console.log("result ->", result);
//     //   });

//     console.log(
//       `ID: ${id}, Name: ${new_prodName}, Price: ${new_prodPrice}, Description: ${new_prodDescpt}`
//     );
//     //Once the post has been submitted, return false to prevent reload.
//     return false;
//   };
// };
