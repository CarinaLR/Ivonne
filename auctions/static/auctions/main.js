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
  return false;
};

// Block to populate textarea that allows user to update product info.

const editProd_view = (response) => {
  // Getting response with information only for product to be edited.
  let prod_id = response.id;
  let edit_name = response.name;
  let edit_price = response.price;
  let edit_descpt = response.description;

  // Get all product information and populate the form to make a put request with updating info.
  let prod_idUpt = (document.querySelector("#prod_idUpt").innerHTML = prod_id);
  let new_name = (document.querySelector(
    "#editProdName"
  ).innerHTML = edit_name);
  let new_price = (document.querySelector(
    "#editProdPrice"
  ).innerHTML = edit_price);
  let new_textarea = (document.querySelector(
    "#editProdDescpt"
  ).innerHTML = edit_descpt);

  // saveUptProd(response.id);
  let id = prod_id;
  let upt_prodName, upt_prodPrice, upt_prodDescpt;

  //On submit, send product info to update product.
  const edit_prod = (document.querySelector(
    "#editProd_form"
  ).onsubmit = async () => {
    try {
      // Get all values from textarea to update content.
      upt_prodName = document.getElementById("editProdName").value;
      new_prodPrice = document.getElementById("editProdPrice").value;
      new_prodDescpt = document.getElementById("editProdDescpt").value;

      const res = await fetch(`/editProduct/${id}`, {
        method: "PUT",
        body: JSON.stringify({
          name: upt_prodName,
          description: upt_prodDescpt,
          price: upt_prodPrice,
        }),
      })
        .then((res) => res.json())
        .then((result) => {
          console.log("result ->", result);
        });
    } catch (err) {
      console.error("err", err);
    }
    console.log(
      `ID: ${id}, Name: ${upt_prodName}, Price: ${upt_prodPrice}, Description: ${upt_prodDescpt}`
    );
    //Once the post has been submitted, return false to prevent reload.
    return false;
  });
  return false;
};
