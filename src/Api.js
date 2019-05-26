import axios from 'axios'

export default () => {
  return axios.create({
    baseURL: 'https://hci-server-uvg.herokuapp.com/'
  })
}