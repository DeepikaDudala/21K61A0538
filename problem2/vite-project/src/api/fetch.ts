export const fetchData = (endpoint: string) => {
	const options = {
		method: 'GET',
	};

	return fetch(endpoint, options)
		.then((response) => response.json())
		.catch((error) => console.log(error));
};
