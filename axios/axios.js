var axios = require("axios");

var config = {
  method: "get",
  url: "http://www.portalmaas.com.br/teste/seggest/server/getLogoAndColorByIdParceiro.php?id_parceiro=dsad",
  headers: {},
};

const request = () => {
  axios(config)
    .then(function (response) {
      console.log(response.data.logo);
    })
    .catch(function (error) {
      console.log(error);
    });
};

request()