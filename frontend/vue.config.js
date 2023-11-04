const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  // generate templates for Flask
  outputDir: "../templates/vue",

  // entrypoint template
  // indexPath: "index.html",

  // generate assets for Flask
  assetsDir: "../../static/vue",

  transpileDependencies: true,

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    },
  },
});
