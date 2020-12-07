// new WOW().init();

// alert("Hello, World");

const update_prod = (prod_id) => {
  // Show more edit profile and hide user profile
  document.querySelector("#add_box").style.display = "none";
  document.querySelector("#edit_box").style.display = "block";

  var updt_id = prod_id;
  console.log(`this is the ${updt_id} updating function`);
  // Fetch data from db to get all products
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

const editProd_view = (response) => {
  console.log("response view- ", response);
};
