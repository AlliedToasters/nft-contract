const Migrations = artifacts.require("Migrations");
const wgmi = artifacts.require("WGMINFT")

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};
