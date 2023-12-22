let data = {
	area: 1,
	dormitorios: 1,
	banheiros: 1,
	vagas: 1
}

const apiUrl = 'http://127.0.0.1:8000/predict'
const requestOptions = {
	method: 'POST',			
	headers: {
		"Content-type": "application/json"
	},
	body: JSON.stringify(data)
}

console.log(requestOptions)

fetch(apiUrl, requestOptions)
	.then(response => {
		if (!response.ok) {
			throw new Error('Erro na requisição');
		}
		return response.json();
	})
	.then(data => {
		console.log('Dados recebidos:', data);
	})
	.catch(error => {
		console.error('Erro:', error);
	});
