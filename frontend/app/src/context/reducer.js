export function reducer (state, action) {
  switch (action.type) {
    case 'setValue': {
      return {...state, ...action.payload }
    }
    default: {
      return state;
    }
  }

}