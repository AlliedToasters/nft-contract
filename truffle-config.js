const path = require("path");
//var HDWalletProvider = require("truffle-hdwallet-provider");
//const MNEMONIC = '<YOUR MNEMONIC HERE>';
const providerAddress = 'https://ropsten.infura.io/v3/e0612a9ac52d4e0ea8b800c5b24e48fb';
const providerAddressRinkeby = 'https://rinkeby.infura.io/v3/a562ea5c4e6a4ab38e9a24fda9148b6f';
const PrivateKeyProvider = require("truffle-privatekey-provider");

const privKey = "129b418a329ebcc7fa541862fc66a82603ccad2786adf15c904bee5512902128";

module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // to customize your Truffle configuration!
  contracts_build_directory: path.join(__dirname, "client/src/contracts"),
  networks: {
    develop: {
      host: "127.0.0.1", // Random IP for example purposes (do not use)
      port: 8545,
      network_id: 1,        // Ethereum public network
      from:"0x5824bcb644835f3f31e0aa8d3f5733a609b6cab8"
    },
    live: {
      host: "127.0.0.1", 
      port: 8545,
      network_id: 15, 
    },
    ropsten: {
      provider: function() {
        return new PrivateKeyProvider(privKey, providerAddress)
      },
      host: "127.0.0.1", // Random IP for example purposes (do not use)
      port: 8545,
      network_id: 3
    },
    rinkeby: {
      provider: function() {
        return new PrivateKeyProvider(privKey, providerAddressRinkeby)
      },
      host: "127.0.0.1", // Random IP for example purposes (do not use)
      port: 8545,
      network_id: 4
    },
    localPrivateNetwork: {
      // provider: function() {
      //   //return new HDWalletProvider(MNEMONIC, "https://ropsten.infura.io/YOUR_API_KEY")
      //   return new HDWalletProvider(MNEMONIC, "https://127.0.0.1:8545")
      // },
      host: "127.0.0.1",
      port: 8545,
      network_id: "*"
    }
  },
  compilers: {
    solc: {
      version: "^0.8.0"
    }
  }
};
