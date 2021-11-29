var wgmi = artifacts.require("./WGMINFT.sol");
var web3 = require("web3")

module.exports = function(deployer) {
  deployer.deploy(
      wgmi, 
      "Unruggable Pheonix", 
      "wgmiphx",
      "https://unruggable-pheonix-web-2-plqvx.ondigitalocean.app/metadata?id=",
      "lmao"
      );
};
