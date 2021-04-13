import React, {useState} from 'react';

function Entity({entity}) {
	const renderData = (data) => {
		const listItems = []
		for (let i = 0; i < data.length; i++){
			if (i < data.length - 1) {
				listItems.push(<>{data[i] + ', '}</>)
			} else {
				listItems.push(<>{data[i]}</>)
			}
		}
		return listItems
	};
	// keywords, location, person
	return (
		<div>
			<h5>Entity</h5>
			<p>
				{entity.date[0] ? <><b>Date: </b>{renderData(entity.date)}</> : ''}
				<br/>
				{entity.keywords[0] ? <><b>Keyword: </b>{renderData(entity.keywords)}</> : ''}
				<br/>
				{entity.location[0] ? <><b>Location: </b>{renderData(entity.location)}</> : ''}
				<br/>
				{entity.person[0] ? <><b>Person: </b>{renderData(entity.person)}</> : ''}
			</p>
		</div>
	);
}

export default Entity;
