new WOW().init();

const loadProducts = () => {
  // Fetch data from db to get all products
  fetch("responseJSON")
    .then((response) => response.json())
    .then((response) => {
      console.log("response - ", response);
    });
};
