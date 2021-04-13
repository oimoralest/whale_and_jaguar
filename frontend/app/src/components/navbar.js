import React, {useState, useContext} from 'react';
import context from '../context';

import axios from 'axios';

function NavBar() {
	const [value, setValue] = useState('');
	const {dispatch} = useContext(context);

	const handleChange = (event) => {
		setValue(event.target.value);
	};

	const handleSubmit = async (event) => {
		event.preventDefault();
		const response = await axios.get(
			`http://192.168.99.101:8000/api/v1/text/count/?count=${value}`,
		);
		dispatch({type: 'setValue', payload: response.data});
	};

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container-fluid">
				<a className="navbar-brand" href="/">
					Text analyzer
				</a>
				<form className="d-flex">
					<input
						className="form-control me-2"
						type="search"
						placeholder="Search for last texts"
						aria-label="Search"
						value={value}
						onChange={handleChange}
						style={{marginRight: "10px"}}
					/>
					<button
						className="btn btn-outline-success"
						type="submit"
						onClick={handleSubmit}
					>
						Search
					</button>
				</form>
			</div>
		</nav>
	);
}

export default NavBar;
