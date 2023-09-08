const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
})

module.exports = {
  configureWebpack: {
    watchOptions: {
      aggregateTimeout: 200,
      poll: 1000,
    },
  }
}
module.exports = {
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    liveReload: true,
  }
}