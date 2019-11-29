import React, { useState } from 'react'
import PropTypes from 'prop-types'

const initialState = {
  text: ''
}

export default function ChatLineForm ({ appendLine }) {
  const [state, setState] = useState(initialState)

  const onSubmit = event => {
    event.preventDefault()
    if (state.text) {
      appendLine({ user: 'You', text: state.text })
      setState({ ...initialState })
    }
  }

  const handleChange = (event) => setState({ text: event.target.value.trim() })

  return (
    <form onSubmit={onSubmit} className="ChatLineForm">
      <input placeholder="Type some text..." type="text" value={state.text} onChange={handleChange} className="ChatLineInput" />
    </form>
  )
}

ChatLineForm.propTypes = {
  appendLine: PropTypes.func
}
