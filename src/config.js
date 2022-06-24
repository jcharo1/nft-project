const basePath = process.cwd();
const { MODE } = require(`${basePath}/constants/blend_mode.js`);
const { NETWORK } = require(`${basePath}/constants/network.js`);

const network = "";

// General metadata for Ethereum
const namePrefix = "Likey";
const description = "I am one of a set of nearly identical clones. I am the first to uncover the truth about my creators. The truth that they were not created for me, but for you...";
// const baseUri = "ipfs://NewUriToReplace";
const baseUri = "ipfs://QmaSnFQnhq7wJCQkugfNymQBRZkmueyJAyRDfWUtZetusG";

const solanaMetadata = {
  symbol: "YC",
  seller_fee_basis_points: 1000, // Define how much % you want from secondary market sales 1000 = 10%
  external_url: "https://likeysworld.com/",
  creators: [
    {
      address: "",
      share: 100,
    },
  ],
};
// If you have selected Solana then the collection starts from 0 automatically
const layerConfigurations = [
  {
    growEditionSizeTo: 777,
    layersOrder: [
      { name: "background solid",  options: {
        bypassDNA: true
    } },
      { name: "background gradient solid",  options: {
        bypassDNA: true
    }  },
      { name: "background artistic",   options: {
        bypassDNA: true
    }  },
      { name: "background spray", 
          options: {
          bypassDNA: true
      } },
      { name: "body"},
      { name: "earrings" },
      { name: "mouths" },
      { name: "eyes" },
      { name: "hair" },
      { name: "clothes" },
    ],
  },
];
const shuffleLayerConfigurations = false;

const debugLogs = false;

const format = {
  width:  4097,
  height:  4097,
  smoothing: false,
};

const gif = {
  export: false,
  repeat: 0,
  quality: 100,
  delay: 500,
};

const text = {
  only: false,
  color: "#ffffff",
  size: 20,
  xGap: 40,
  yGap: 40,
  align: "left",
  baseline: "top",
  weight: "regular",
  family: "Courier",
  spacer: " => ",
};

const pixelFormat = {
  ratio: 2 / 128,
};

const background = {
  generate: true,
  brightness: "80%",
  static: false,
  default: "#000000",
};

const extraMetadata = {};

const rarityDelimiter = ">";

const uniqueDnaTorrance = 10000;

const preview = {
  thumbPerRow: 5,
  thumbWidth: 50,
  imageRatio: format.height / format.width,
  imageName: "preview.png",
};

const preview_gif = {
  numberOfImages: 5,
  order: "ASC", // ASC, DESC, MIXED
  repeat: 0,
  quality: 100,
  delay: 500,
  imageName: "preview.gif",
};

module.exports = {
  format,
  baseUri,
  description,
  background,
  uniqueDnaTorrance,
  layerConfigurations,
  rarityDelimiter,
  preview,
  shuffleLayerConfigurations,
  debugLogs,
  extraMetadata,
  pixelFormat,
  text,
  namePrefix,
  network,
  solanaMetadata,
  gif,
  preview_gif,
};
