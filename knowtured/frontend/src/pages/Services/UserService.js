
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class UserService{
	


    constructor(){}

	getUsers() {
        console.log("get usuarios");
		const url = `${API_URL}/users/`;
		return axios.get(url).then(response => response.data);
	}


	getUser(pk) {
		const url = `${API_URL}/users/${pk}`;
		return axios.get(url).then(response => response.data);
	}

	deleteUsuario(user){
		const url = `${API_URL}/users/${user.pk}`;
		return axios.delete(url);
	}

	createUser(user){
		const url = `${API_URL}/users/`;
		return axios.post(url,user);
	}

	updateUser(user){
		const url = `${API_URL}/users/${user.pk}`;
		return axios.put(url,user);
	}
}
