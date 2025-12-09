// Binance HMAC SHA256 Signature Generation (Node.js)
const crypto = require('crypto')
const axios = require('axios')

class BinanceAPI {
  constructor(apiKey, apiSecret) {
    this.apiKey = apiKey
    this.apiSecret = apiSecret
    this.baseURL = 'https://api.binance.com'
  }

  generateSignature(queryString) {
    return crypto.createHmac('sha256', this.apiSecret).update(queryString).digest('hex')
  }

  async getAccountBalance() {
    const timestamp = Date.now()
    const queryString = `timestamp=${timestamp}&recvWindow=5000`
    const signature = this.generateSignature(queryString)

    try {
      const response = await axios.get(`${this.baseURL}/api/v3/account`, {
        params: { timestamp, recvWindow: 5000, signature },
        headers: { 'X-MBX-APIKEY': this.apiKey }
      })
      return response.data
    } catch (error) {
      if (error.response?.data?.code === -1021) {
        // Handle timestamp error - sync time and retry
        console.log('Timestamp error, syncing and retrying...')
        // Retry logic here
      }
      throw error
    }
  }

  async createMarketOrder(symbol, side, quantity) {
    const timestamp = Date.now()
    const params = {
      symbol,
      side,
      type: 'MARKET',
      quantity,
      timestamp,
      recvWindow: 5000
    }

    const queryString = Object.keys(params)
      .map((key) => `${key}=${params[key]}`)
      .join('&')
    const signature = this.generateSignature(queryString)

    const response = await axios.post(`${this.baseURL}/api/v3/order`, null, {
      params: { ...params, signature },
      headers: { 'X-MBX-APIKEY': this.apiKey }
    })

    return response.data
  }
}

module.exports = BinanceAPI
