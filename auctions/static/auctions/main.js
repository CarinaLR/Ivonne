// new WOW().init();

// alert("Hello, World");

//Forms are at risk for Cross Site Request Forgeries (CSRF) attacks. When it comes to AJAX requests, we need to add custom header that includes the token to watch our back.
// Acquiring the token (cookie)
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie("csrftoken");

// Stop page to resubmit form and refresh
const handleForm = (event) => {
  event.preventDefault();
};

const callingFalse = () => {
  console.log("Reach callingFalse");
  return false;
};

// Block to show and hide respective view

const update_prod = (prod_id) => {
  // Show edit form and hide add form
  document.querySelector("#add_box").style.display = "none";
  document.querySelector("#edit_box").style.display = "block";

  get_ProdData(prod_id);

  return false;
};

// Block to fetch data from db to get all products and send response only with selected product.

const get_ProdData = (prod_id) => {
  var updt_id = prod_id;
  console.log(`this is the ${updt_id} updating function`);

  fetch("responseJSON")
    .then((response) => response.json())
    .then((response) => {
      for (i = 0; i < response.length; i++) {
        let prod = response[i];
        if (prod.id === updt_id) {
          // editProd_view(prod);
          showsData(prod);
        }
      }
    });
  return false;
};

// Set global varibles to use in form submition
var id, upt_prodName, upt_prodPrice, upt_prodDescpt;

// Block to populate textarea that allows user to update product info.

// const editProd_view = (response) => {
//   // Getting response with information only for product to be edited.
//   let prod_id = response.id;
//   let edit_name = response.name;
//   let edit_price = response.price;
//   let edit_descpt = response.description;

//   // Get all product information and populate the form to make a put request with updating info.
//   let prod_idUpt = (document.querySelector("#prod_idUpt").innerHTML = prod_id);
//   let new_name = (document.querySelector(
//     "#editProdName"
//   ).innerHTML = edit_name);
//   let new_price = (document.querySelector(
//     "#editProdPrice"
//   ).innerHTML = edit_price);
//   let new_textarea = (document.querySelector(
//     "#editProdDescpt"
//   ).innerHTML = edit_descpt);

//   // saveUptProd(response.id);
//   id = prod_id;
//   // let id = prod_id;
//   // let upt_prodName, upt_prodPrice, upt_prodDescpt;

//   //On submit, send product info to update product.
//   const edit_prod = (document.querySelector(
//     "#editProd_form"
//   ).onsubmit = async () => {
//     try {
//       // Get all values from textarea to update content.
//       upt_prodName = document.getElementById("editProdName").value;
//       new_prodPrice = document.getElementById("editProdPrice").value;
//       new_prodDescpt = document.getElementById("editProdDescpt").value;

//       console.log(
//         `ID: ${id}, Name: ${upt_prodName}, Price: ${upt_prodPrice}, Description: ${upt_prodDescpt}`
//       );

//       const res = await fetch(
//         `/editProduct/${id}`,
//         {
//           method: "PUT",
//           headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": getCookie("csrftoken"),
//           },
//           body: JSON.stringify({
//             description: upt_prodDescpt,
//             name: upt_prodName,
//             price: upt_prodPrice,
//           }),
//         },
//         console.log("FETCH PUT DONE")
//       )
//         .then((res) => res.json())
//         .then((result) => {
//           console.log("result ->", result);
//         });
//     } catch (err) {
//       console.error("err", err);
//     }
//     //Once the post has been submitted, return false to prevent reload.
//     console.log("Still in the form");
//     edit_prod.handleForm();
//     return false;
//   });
//   console.log("Closing the form");
//   return false;
// };

//POPULATE DATA
function showsData(response) {
  console.log("response writeMessage ", response);

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
  id = prod_id;
  document
    .querySelector("#upt_button")
    .addEventListener("click", () => putHTTPRqt(id));
}

//Put request with onclick
function putHTTPRqt(id) {
  // Get values from input to update content
  // Get all values from textarea to update content.
  upt_prodName = document.getElementById("editProdName").value;
  new_prodPrice = document.getElementById("editProdPrice").value;
  new_prodDescpt = document.getElementById("editProdDescpt").value;

  console.log(
    `ID: ${id}, Name: ${upt_prodName}, Price: ${upt_prodPrice}, Description: ${upt_prodDescpt}`
  );

  //PUT request to update.
  fetch(
    `/editProduct/${id}`,
    {
      method: "PUT",
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      body: JSON.stringify({
        description: upt_prodDescpt,
        name: upt_prodName,
        price: upt_prodPrice,
      }),
    },
    console.log("FETCH PUT DONE")
  )
    .then((response) => response.json())
    .then((result) => {
      console.log("result ->", result);
    });

  //Callback to activate alert.
  messageSent();

  //Prevent reloading the page
  return false;
}

function messageSent() {
  alert("Change sent successfully. Thank you!");
  return false;
}

//Set global variable to add count to cart in navbar
var addCount = 0;

// Block to count item and display in the navbar to show qty.

const add_toCart = () => {
  console.log("reach count");
  addCount += 1;
  document.querySelector("#count").innerHTML = addCount;
};

// Block to send product description to toggle button

const get_ProdDescpt = (prod_id) => {
  var showprod_id = prod_id;
  console.log(`this is the ${showprod_id} updating function`);

  fetch("responseJSON")
    .then((response) => response.json())
    .then((response) => {
      for (i = 0; i < response.length; i++) {
        let prod = response[i];
        if (prod.id === showprod_id) {
          createProd_DescptView(prod);
        }
      }
    });
  return false;
};

// Creating Div to append component to each item

const createProd_DescptView = (prod) => {
  var toCheck = prod;
  let prod_dscpt = toCheck.description;

  let toggleCard = document.createElement("div");
  toggleCard.className = "collapse";
  toggleCard.id = "collapseExample";

  let toggleDescpt = document.createElement("div");
  toggleDescpt.className = "card card-body";
  toggleDescpt.innerHTML = prod_dscpt;

  toggleCard.appendChild(toggleDescpt);
  document.getElementById("#prod_Div").appendChild(toggleCard);
};
