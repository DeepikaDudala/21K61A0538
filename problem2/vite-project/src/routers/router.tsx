import { createBrowserRouter } from 'react-router-dom';
import Product from '../pages/Product';
import Products from '../pages/Products';
const router = createBrowserRouter([
	{
		path: '/',
		element: <Products />,
	},
	{
		path: '/:id',
		element: <Product />,
	},
]);

export default router;
