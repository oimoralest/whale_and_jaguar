import React, { useReducer } from 'react';
import NavBar from './components/navbar'
import TextList from './components/textList'
import context from './context/'
import { reducer } from './context/reducer'

function App() {
  const [state, dispatch] = useReducer(reducer, {})
	return (
    <context.Provider value={{state, dispatch}}>
      <div>
        <NavBar />
      </div>
      <div>
        <TextList />
      </div>
    </context.Provider>
  )
}

export default App;
