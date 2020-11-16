import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class CategoriasService{
	


    constructor(){}

	getCategorias() {
        console.log("get categorias");
		const url = `${API_URL}/categorias/`;
		return axios.get(url).then(response => response.data);
	}

	getCategoriasByURL(link){
		const url = `${API_URL}${link}`;
		return axios.get(url).then(response => response.data);
	}

	getCategoria(pk) {
		const url = `${API_URL}/categorias/${pk}`;
		return axios.get(url).then(response => response.data);
	}

	deleteCategoria(categoria){
		const url = `${API_URL}/categorias/${categoria.pk}`;
		return axios.delete(url);
	}

	createCategoria(categoria){
		const url = `${API_URL}/categorias/`;
		return axios.post(url,categoria);
	}

	updateCategoria(categoria){
		const url = `${API_URL}/categorias/${categoria.pk}`;
		return axios.put(url,categoria);
	}
}
