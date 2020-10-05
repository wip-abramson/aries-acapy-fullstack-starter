import axios from 'axios'

const base_endpoint = process.env.NODE_ENV === 'production' ? 'http://194.61.21.227:8000' :  'http://0.0.0.0:8000'
// const base_endpoint = 'http://194.61.20.127:8000'
export const apiInstance = axios.create({
    baseURL: base_endpoint
});
