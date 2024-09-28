import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:5000',
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },
    timeout: 10000
})

export default {
    // add JWT token to the header
    addtoken() {
        const token = localStorage.getItem('token') || sessionStorage.getItem('token');
        if (token) {
          apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          console.log('apiclient header token added', apiClient.defaults.headers.common['Authorization']);
      }
    },
    postUserSignup(signup_user) {
        return apiClient.post('/userSignup', signup_user)
      },
    postUserLogin(login_user) {
      return apiClient.post('/userLogin', login_user)
    }
}