module.exports = {
    devServer: {
        port: 80,
        disableHostCheck: true,
        proxy: {
            '/api': {
                target: 'http://backend:5000',
                secure: false
            }
        }
    }
}
