import React, {useContext} from 'react';
import context from '../context';
import Entity from './entity';
import Sentiment from './sentiment';

function TextList() {
	const {state} = useContext(context);
	return (
		<div className="container" style={{marginTop: '20px'}}>
			{state &&
				state.texts &&
				state.texts.map((text) => (
					<div
						className="card"
						style={{
							marginBottom: '20px',
							borderRadius: '10px',
							color: '#616161',
							border: 'solid 1px #9E9E9E',
						}}
					>
						<div className="card-body">
							<div
								style={{
									display: 'flex',
									justifyContent: 'space-between',
									padding: '10px',
									alignItems: 'flex-end',
								}}
							>
								<h4 style={{margin: '0'}}>Text</h4>
								<p style={{margin: '0'}}>Created at: {text.created_at} </p>
							</div>
							<div
								className="card-text"
								style={{
									border: 'solid 1px #9E9E9E',
									borderRadius: '10px',
									padding: '10px',
									backgroundColor: '#f8f9fa',
								}}
							>
								<p
									style={{
										textAlign: 'justify',
										textJustify: 'inter-word',
									}}
								>
									{text.text}
								</p>
								<Sentiment sentiment={text.sentiment} />
								<Entity entity={text.entity} />
							</div>
						</div>
					</div>
				))}
		</div>
	);
}

export default TextList;
