import React, {useState} from 'react';

function Sentiment({sentiment}) {
	return (
		<div>
			<h5>Sentiment</h5>
			<p>
				{sentiment.polarity ? <><b>Polarity: </b>{sentiment.polarity}</> : ''}
                <br/>
                {sentiment.subjectivity ? <><b>Subjectivity: </b>{sentiment.subjectivity}</> : ''}
                <br/>
                {sentiment.polarity_confidence ? <><b>Polarity confidence: </b>{sentiment.polarity_confidence}</> : ''}
                <br/>
                {sentiment.subjectivity_confidence ? <><b>Subjectivity confidence: </b>{sentiment.subjectivity_confidence}</> : ''}
			</p>
		</div>
	);
}

export default Sentiment;