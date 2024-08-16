import React, { useEffect } from 'react';

const Products: React.FC = () => {
	useEffect(() => {
		const data = fetch('http://localhost:8000/products');
	}, []);
	return (
		<div>
			<h1>Products</h1>
		</div>
	);
};

export default Products;
